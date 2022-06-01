#!/usr/bin/env python3.10

import os
from flask import Flask
from storage import inc_counter

port = os.getenv('PORT', 5555)
app = Flask(__name__)


@app.route('/pingpong', methods=['GET'])
def main():
    count = inc_counter()
    return f'{count}'
