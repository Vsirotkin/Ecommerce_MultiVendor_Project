FROM python:3.10.6-alpine

COPY requirements.txt /temp/requirements.txt
COPY eshop /eshop
WORKDIR /eshop
EXPOSE 8000

#RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password eshop-user

USER eshop-user
