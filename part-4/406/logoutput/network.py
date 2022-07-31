import urllib.request
from typing import List
import json

from storage import IMAGE_PATH
import requests

IMAGE_URL = "https://picsum.photos/400.jpg"


def get_todos() -> List[str]:
    todos = requests.get('http://todoapp-svc:4444/todos')
    return json.loads(todos.text)


def add_item_to_todo(item) -> None:
    requests.post('http://todoapp-svc:4444/todos', json={'item': item})


def toggle_todo(is_done: bool, id: int) -> bool:
    response = requests.put(f'http://todoapp-svc:4444/todos/{id}', json={'is_done': is_done})
    return response.ok


def download_image() -> None:
    urllib.request.urlretrieve(IMAGE_URL, IMAGE_PATH)


def read_pongs() -> str:
    x = requests.get('http://pingpong-svc/pingpong')
    return x.text


def check_pingpong() -> int:
    """
    Make a test connection to the pingpong application
    :return: status code of the response
    """
    try:
        code = requests.get('http://pingpong-svc/pingpong', timeout=10).status_code
        return code
    except requests.RequestException:
        return 400
