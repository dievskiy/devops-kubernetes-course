FROM python:3.10

LABEL maintainer="Ruslan Potekhin <potekhin.ruslan@gmail.com>"

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY . .

RUN apt-get update && \
      apt-get -y install sudo

RUN useradd -rm -d /home/python -s /bin/bash -g root -G sudo -u 1001 python && \
     echo "python:python" | chpasswd

RUN pip install --no-cache-dir -r requirements.txt

USER python

CMD uwsgi --workers 1 --threads 1 --http 0.0.0.0:${PORT:-5555} --module app:app