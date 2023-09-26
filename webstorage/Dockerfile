FROM docker.io/python:3.9.6-buster

RUN mkdir /opt/webstorage

ADD requirements.txt /opt/webstorage

WORKDIR /opt/webstorage

RUN pip install -r requirements.txt

ADD . /opt/webstorage

ENTRYPOINT ["gunicorn", "webstorage:app"]
CMD ["--bind=0.0.0.0:8080", "--access-logfile=-"]

