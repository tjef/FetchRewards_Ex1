#Dockerfile , Image, Container Image

FROM python:3.8

WORKDIR /flask-app

COPY req.txt .

RUN pip install -r req.txt

COPY ./app ./app

CMD ["python" , "./app/main.py"]




