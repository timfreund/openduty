FROM python:2

RUN apt-get update && apt-get install -y build-essential libmysqlclient-dev libldap2-dev libsasl2-dev python-pip python-setuptools mysql-client

WORKDIR /usr/src/app

RUN pip install gunicorn
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

EXPOSE 8000
COPY . /usr/src/app
ENV DJANGO_SETTINGS_MODULE openduty.settings_docker
CMD python manage.py runserver 0.0.0.0:8000
