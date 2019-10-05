FROM python:3.6-alpine3.6

RUN pip3 install flask flask-sqlalchemy && \
    pip3 install virtualenv

ADD infinite.sh /infinite.sh
WORKDIR /app
ENTRYPOINT [ "/bin/sh","/infinite.sh" ]