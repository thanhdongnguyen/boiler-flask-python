FROM python:3.7-alpine3.10

COPY ./server/src/setup.py /setup.py

RUN pip install setuptools

RUN apk add --no-cache vim curl bash gcc jpeg-dev zlib-dev musl-dev

RUN python /setup.py install
