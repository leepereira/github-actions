# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY ./function/requirements.txt requirements.txt
COPY ./function/app.py app.py
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--port=8080", "--host=0.0.0.0"]