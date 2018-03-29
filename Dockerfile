FROM python:alpine3.4
MAINTAINER Clint Mann "climann2@cisco.com"


ADD . /app

WORKDIR /app

RUN pip install -r /fingerprint-app/requirements.txt

CMD [ "python", "./fingerprint-app/monitorspark.py" ]