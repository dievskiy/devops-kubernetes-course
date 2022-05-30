#!/usr/bin/env python3.10

import os
from flask import Flask
from storage import write_to_file

port = os.getenv('PORT', 5555)
app = Flask(__name__)

counter = 0


@app.route('/pingpong', methods=['GET'])
def main():
    global counter
    counter += 1
    write_to_file(counter)
    return '', 204
