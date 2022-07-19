#!/usr/bin/env python3.10

from flask import Flask, jsonify
from storage import inc_counter, init_db, check_connection

app = Flask(__name__)


@app.route('/healthz', methods=['GET'])
def health():
    """
    Check that the app has established a connection to the database
    :return: 200 on success, 400 otherwise
    """
    if check_connection():
        return jsonify({'message': 'ok'}), 200
    else:
        return jsonify({'message': 'error'}), 400


@app.route('/pingpong', methods=['GET'])
def main():
    count = inc_counter()
    return f'{count}'


init_db()
