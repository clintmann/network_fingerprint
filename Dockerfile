FROM python:2.7-alpine
MAINTAINER Clint Mann "climann2@cisco.com"


ADD . /app

WORKDIR /app

RUN pip install -r /fingerprint-app/requirements.txt

CMD [ "python", "./finerprint-app/monitorspark.py" ]