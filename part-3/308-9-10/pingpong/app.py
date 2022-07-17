#!/usr/bin/env python3.10

from flask import Flask
from storage import inc_counter, init_db
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def healthcheck():
    return json.dumps({'message': 'ok'}), 200, {'ContentType': 'application/json'}


@app.route('/pingpong', methods=['GET'])
def main():
    count = inc_counter()
    return f'{count}'


init_db()
