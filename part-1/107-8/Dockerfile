FROM python:3.8

LABEL maintainer="Ruslan Potekhin <potekhin.ruslan@gmail.com>"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -rm -d /home/python -s /bin/bash -g root -G sudo -u 1001 python

USER python

CMD uwsgi --master --workers 4 --threads 8 --http 0.0.0.0:${PORT:-3333} --module app:app