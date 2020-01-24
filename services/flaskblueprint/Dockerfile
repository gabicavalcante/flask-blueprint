# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.8.0-alpine

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=flaskblueprint Version=0.0.1
EXPOSE 5000

# copy project
COPY . /flaskblueprint

# set work directory
WORKDIR /flaskblueprint 

# set environment variables
# Prevents Python from writing pyc files to disc 
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr 
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev libffi-dev  musl-dev

# Using pip:
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt 

#RUN cp .env.sample .env
#RUN cp .secrets.toml.sample .secrets.toml

# run entrypoint.sh
CMD ["/entrypoint.sh"]

# Using pipenv:
#RUN pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "flaskblueprint"]

