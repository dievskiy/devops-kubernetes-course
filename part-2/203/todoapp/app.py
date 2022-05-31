#!/usr/bin/env python3.10

import os
from flask import Flask, request

port = os.getenv('PORT', 4444)
app = Flask(__name__)
todos = []


@app.route('/todos', methods=['GET', 'POST'])
def get_todos():
    global todos
    if request.method == 'POST':
        body = request.json
        todos.append(body['item'])
        return '', 204
    else:
        return f'{todos}'
