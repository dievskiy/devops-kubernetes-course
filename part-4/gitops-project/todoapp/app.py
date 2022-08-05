#!/usr/bin/env python3.9

import os
from aioflask import Flask, request, jsonify
from storage import save_todo, fetch_todos, check_connection, toggle
from publish import publish_todo

port = os.getenv('PORT', 4444)
app = Flask(__name__)


def is_valid(item: str) -> bool:
    return 0 < len(item) < 140


@app.route('/healthz')
def health():
    """
    Check that the app has established a connection to the database
    :return: 200 on success, 400 otherwise
    """
    if check_connection():
        return jsonify({'message': 'ok'}), 200
    else:
        return jsonify({'message': 'error'}), 400


@app.route('/todos/<id>', methods=['PUT'])
async def toggle_todo(id):
    body = request.json
    if not body.__contains__('is_done'):
        return jsonify({'message': f'Todo status was not specified'}), 400
    is_done = bool(body['is_done'])
    res = toggle(int(id), is_done)
    if res:
        await publish_todo(f'Todo with id {id}', 'done')
        return jsonify({}), 204
    else:
        return jsonify({'message': f'Failed to set todo "{id} as {is_done}"'}), 400


@app.route('/todos', methods=['GET'])
def get_todos():
    todos = fetch_todos()
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
async def add_todo():
    body = request.json
    if not body.__contains__('item'):
        return jsonify({'message': f'Item name was not specified'}), 400
    new_todo = body['item']
    if not is_valid(new_todo):
        print('Todo is invalid, longer than 140 symbols')
        return jsonify({'message': 'Todo content is too long'}), 400
    save_todo(new_todo)
    await publish_todo(new_todo, 'created')
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, port=port, host='0.0.0.0')
