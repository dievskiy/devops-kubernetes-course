#!/usr/bin/env python3.10

import os
from flask import Flask, request, jsonify
from storage import save_todo, fetch_todos, init_db, check_connection

port = os.getenv('PORT', 4444)
app = Flask(__name__)


def is_valid(item: str) -> bool:
    return 0 < len(item) < 140


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


@app.route('/todos', methods=['GET', 'POST'])
def get_todos():
    if request.method == 'POST':
        body = request.json
        new_todo = body['item']
        if not is_valid(new_todo):
            print('Todo is invalid, longer than 140 symbols')
            return jsonify({'message': 'Todo content is too long'}), 400
        save_todo(new_todo)
        return '', 204
    else:
        todos = fetch_todos()
        return f'{todos}'


init_db()
