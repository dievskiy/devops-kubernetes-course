import urllib.request
from typing import List

from storage import IMAGE_PATH
import requests

IMAGE_URL = "https://picsum.photos/400.jpg"


def get_todos() -> List[str]:
    todos = requests.get('http://todoapp-svc:4444/todos')
    return todos.text.replace("[", "").replace("]", "").replace("'", "").split(",")


def add_item_to_todo(item) -> None:
    requests.post('http://todoapp-svc:4444/todos', json={'item': item})


def download_image() -> None:
    urllib.request.urlretrieve(IMAGE_URL, IMAGE_PATH)


def read_pongs() -> str:
    x = requests.get('http://pingpong-svc/pingpong')
    return x.text
