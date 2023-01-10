FROM python:3.10.6-alpine
ENV PUTHONUNBUFFERED 1

WORKDIR /eshop

COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
