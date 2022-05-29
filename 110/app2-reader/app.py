#!/usr/bin/env python3.10

# This app generates a new timestamp every 5 seconds and saves it into a file /usr/src/app/files/logs.txt

import os
from flask import Flask, make_response
from storage import read_timestamp_from_file, FileError
from hash import generate_random_string

port = os.getenv('PORT', 5555)
app = Flask(__name__)


@app.route('/output', methods=['GET'])
def output():
    h = generate_random_string()
    try:
        timestamp = read_timestamp_from_file()
    except FileError:
        raise FileError()
    return make_response(f"Hash : {h}, timestamp: {timestamp}")
