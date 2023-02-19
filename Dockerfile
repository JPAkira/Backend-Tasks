FROM  python:3.8.3-slim as python-base

RUN apt-get update

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt

copy * ./

copy /tasks ./tasks

RUN whoami

RUN python manage.py collectstatic

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--worker-class", "uvicorn.workers.UvicornWorker", "--timeout", "15", "--workers", "3", "tasks.routing:application", "--access-logfile", "-", "--error-logfile", "-"]
