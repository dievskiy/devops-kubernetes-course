#!/usr/bin/env python3.10

import datetime
import os
from dotenv import load_dotenv

from flask import (Flask, render_template, request)
from network import download_image
from hash import generate_random_string
from network import read_pongs, add_item_to_todo
from storage import is_image_present, read_image

port = os.getenv('PORT', 3333)
app = Flask(__name__)

load_dotenv("/config/.env")

MESSAGE = os.getenv('MESSAGE')

if not MESSAGE:
    print("MESSAGE variable is empty")
    exit(1)


def get_message() -> str:
    return MESSAGE


def print_port() -> None:
    print(f'Server started in port {port}')


@app.route('/submit_form')
def form():
    item = request.args.get('item')
    add_item_to_todo(item)
    return '', 200


@app.route('/', methods=['GET'])
def main():
    if not is_image_present():
        download_image()
    image = read_image()
    message = get_message()
    return render_template('index.html',
                           current_time=str(datetime.datetime.now()),
                           random_string=generate_random_string(),
                           pongs=read_pongs(),
                           image_data=image.decode('utf-8'),
                           message=message
                           )


print_port()
