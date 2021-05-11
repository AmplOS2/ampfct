FROM python:buster

RUN apt install -y imagemagick
RUN pip3 install Pillow bitarray

VOLUME /ampfct
WORKDIR /ampfct
