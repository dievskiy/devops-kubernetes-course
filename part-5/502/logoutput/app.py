#!/usr/bin/env python3.10

import datetime
import os

from dotenv import load_dotenv
from flask import (Flask, render_template, request, jsonify, redirect, url_for)

from hash import generate_random_string
from network import download_image
from network import read_pongs, add_item_to_todo, get_todos, check_pingpong, toggle_todo
from storage import is_image_present, read_image

port = os.getenv('PORT', 3333)
app = Flask(__name__)

load_dotenv("/config/.env")

MESSAGE = os.getenv('MESSAGE')

if not MESSAGE:
    print("MESSAGE variable is empty")
    exit(1)


def get_message() -> str:
    return MESSAGE


def print_port() -> None:
    print(f'Server started in port {port}')


@app.route('/healthz')
def health():
    """
    Check that the app has started successfully by verifying that
    connection to pingpong has been established
    :return: 200 on success, 400 otherwise
    """
    if check_pingpong() == 200:
        return jsonify({'message': 'ok'}), 200
    else:
        return jsonify({'message': 'error'}), 400


@app.route('/submit_form', methods=['POST'])
def form_add_item():
    item = request.form['item']
    print(f"Adding {item}")
    add_item_to_todo(item)
    return redirect(url_for('main'))


@app.route('/form_toggle_todo/<todo_id>', methods=['POST'])
def form_toggle_todo(todo_id):
    if todo_id:
        toggle_todo(True, int(todo_id))
    return redirect(url_for('main'))


@app.route('/', methods=['GET'])
def main():
    if not is_image_present():
        download_image()
    image = read_image()
    message = get_message()
    return render_template('index.html',
                           current_time=str(datetime.datetime.now()),
                           random_string=generate_random_string(),
                           pongs=read_pongs(),
                           image_data=image.decode('utf-8'),
                           message=message,
                           todos=get_todos()
                           )


def fix_folder_permission():
    # dirty hack but don't want to spend time on this
    os.system('echo %s|sudo -S %s' % ("python", "chown -R python:python /usr/src/app/files"))
    os.system('echo %s|sudo -S %s' % ("python", "chown -R python:python /usr/src/app/files"))


fix_folder_permission()
print_port()
