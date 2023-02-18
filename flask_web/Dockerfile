FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]