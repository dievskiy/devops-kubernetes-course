FROM python:3.8

LABEL maintainer="Ruslan Potekhin <potekhin.ruslan@gmail.com>"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt && \
    apt-get update -y && \
    apt-get install -y sudo && \
    useradd -m python && echo "python:python" | chpasswd && adduser python sudo

COPY . .

USER python

CMD uwsgi --workers 1 --threads 1 --http 0.0.0.0:${PORT:-3333} --module app:app