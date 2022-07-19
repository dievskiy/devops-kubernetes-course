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


def check_pingpong() -> int:
    """
    Make a test connection to the pingpong application
    :return: status code of the response
    """
    try:
        code = requests.get('http://pingpong-svc/pingpong', timeout=2).status_code
        return code
    except requests.RequestException:
        return 400
