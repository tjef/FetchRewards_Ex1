#Dockerfile , Image, Container Image

FROM python:3.8

ADD example1.py .
RUN pip install numpy

CMD ["python" , "./example1.py"]

