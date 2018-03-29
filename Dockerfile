FROM alpine:3.5
MAINTAINER Clint Mann "climann2@cisco.com"


ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python3", "./finerprint-app/monitorspark.py" ]