# pull official base image
FROM python:3.8.3-alpine
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# set work directory
RUN mkdir /code
WORKDIR /code
RUN apk update && apk --no-cache add gcc musl-dev libjpeg-turbo-dev libxslt-dev python3-dev bzip2 tzdata

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt