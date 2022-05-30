#!/usr/bin/env python3

import datetime
import os
import uuid

from flask import make_response, jsonify, Flask

port = os.environ['PORT']
app = Flask(__name__)


def generate_random_string() -> str:
    """
    Generates random string
    """
    return str(uuid.uuid4())


def print_port():
    print(f'Server started in port {port}')


@app.route('/', methods=['GET'])
def index():
    resp = make_response(
        jsonify(
            {'message': f'{datetime.datetime.now()}: '
                        f'{generate_random_string()}'}
        )
    )
    resp.headers['Content-Type'] = 'application/json'
    return resp


print_port()
