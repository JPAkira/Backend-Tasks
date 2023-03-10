FROM  python:3.8.3-slim as python-base

ARG DATABASE_HOST
ARG DATABASE_USER
ARG DATABASE_PASSWORD

ENV DATABASE_HOST=$DATABASE_HOST \
    DATABASE_USER=$DATABASE_USER \
    DATABASE_PASSWORD=$DATABASE_PASSWORD \
    PYTHONUNBUFFERED=1
    
RUN echo "teste $DATABASE_PASSWORD"

RUN apt-get update

RUN apt-get install python3-venv -y

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

copy * ./

copy /tasks ./tasks

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "tasks.wsgi"]
