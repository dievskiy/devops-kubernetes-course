#!/usr/bin/env python3.10

import os
from flask import Flask, request
from storage import save_todo, fetch_todos

port = os.getenv('PORT', 4444)
app = Flask(__name__)


@app.route('/todos', methods=['GET', 'POST'])
def get_todos():
    if request.method == 'POST':
        body = request.json
        new_todo = body['item']
        save_todo(new_todo)
        return '', 204
    else:
        todos = fetch_todos()
        return f'{todos}'
