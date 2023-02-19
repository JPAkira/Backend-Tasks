FROM  python:3.8.3-slim as python-base

ARG DATABASE_HOST
ARG DATABASE_USER
ARG DATABASE_PASSWORD

ENV DATABASE_HOST=$DATABASE_HOST \
    DATABASE_USER=$DATABASE_USER \
    DATABASE_PASSWORD=$DATABASE_PASSWORD
    
RUN echo "teste $DATABASE_PASSWORD"

RUN apt-get update

RUN apt-get install python3-venv

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN python -m venv .venv

RUN source .venv/bin/activate

RUN ./.venv/

RUN pip install -r requirements.txt

copy * ./

copy /tasks ./tasks

RUN whoami

RUN python manage.py collectstatic

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--worker-class", "uvicorn.workers.UvicornWorker", "--timeout", "15", "--workers", "3", "tasks.routing:application", "--access-logfile", "-", "--error-logfile", "-"]
