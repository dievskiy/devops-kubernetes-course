#!/usr/bin/env python3.10

from flask import Flask
from storage import inc_counter
import json

app = Flask(__name__)


# won't be accessed through ingress in this case, but let it be here
# also, in log-output there's no connection with todo service, as it was
# not required
@app.route('/', methods=['GET'])
def healthcheck():
    return json.dumps({'message': 'ok'}), 200, {'ContentType': 'application/json'}


@app.route('/pingpong', methods=['GET'])
def main():
    count = inc_counter()
    return f'{count}'
