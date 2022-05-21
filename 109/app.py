#!/usr/bin/env python3

import os

from flask import (Flask, make_response)

port = os.getenv('PORT', 5555)
app = Flask(__name__)

counter = 0


@app.route('/pingpong', methods=['GET'])
def main():
    global counter
    response = make_response(f"pong {counter}")
    counter += 1
    return response
