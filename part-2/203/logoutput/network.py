import urllib.request
from storage import IMAGE_PATH
import requests

IMAGE_URL = "https://picsum.photos/400.jpg"


def add_item_to_todo(item) -> None:
    requests.post('http://todoapp-v1-svc:1010/todos', json={'item': item})


def download_image() -> None:
    urllib.request.urlretrieve(IMAGE_URL, IMAGE_PATH)


def read_pongs() -> str:
    x = requests.get('http://pingpong-v3-svc:1111/pingpong')
    return x.text
