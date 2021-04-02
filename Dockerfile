FROM python:3.8

MAINTAINER ragh, raghav.ajay3@gmail.com

WORKDIR /usr/irisdeployment

EXPOSE 8080

COPY requirements.txt

RUN pip install -r requirements.txt

CMD python flaskapp.py