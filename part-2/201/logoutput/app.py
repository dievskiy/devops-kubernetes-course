#!/usr/bin/env python3.10

import datetime
import os

from flask import (Flask, render_template)

from hash import generate_random_string
from network import read_pongs

port = os.getenv('PORT', 3333)
app = Flask(__name__)


def print_port() -> None:
    print(f'Server started in port {port}')


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html',
                           current_time=str(datetime.datetime.now()),
                           random_string=generate_random_string(),
                           pongs=read_pongs(),
                           )


print_port()
