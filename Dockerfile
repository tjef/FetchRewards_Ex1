#Dockerfile , Image, Container Image

FROM python:3.8

ADD main.py .
RUN pip install numpy ast json example1 
CMD ["python" , "./main.py"]


