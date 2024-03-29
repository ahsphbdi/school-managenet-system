FROM python:3.11.4-alpine

RUN mkdir /lms
WORKDIR /lms

ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONUNBUFFERED 1

RUN apk add libpq-dev python3-dev
# RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app/* .
