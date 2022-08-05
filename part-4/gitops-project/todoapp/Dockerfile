FROM python:3.10

LABEL maintainer="Ruslan Potekhin <potekhin.ruslan@gmail.com>"

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY . .

RUN apt-get update && \
    apt-get install -y python3-pip && \
    apt install gcc && \
    pip3 install uwsgi && \
    apt-get -y install sudo

RUN pip install -r requirements.txt

RUN useradd -rm -d /home/python -s /bin/bash -g root -G sudo -u 1001 python && \
     echo "python:python" | chpasswd

EXPOSE 4444

USER python

CMD python app.py