#!/usr/bin/env python3

import datetime
import os
import uuid

from flask import (Flask, render_template)

port = os.getenv('PORT', 3333)
app = Flask(__name__)


def generate_random_string() -> str:
    """
    Generates random string
    """
    return str(uuid.uuid4())


def print_port():
    print(f'Server started in port {port}')


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html',
                           current_time=str(datetime.datetime.now()),
                           initial_string=initial_string
                           )


initial_string = generate_random_string()
print_port()
