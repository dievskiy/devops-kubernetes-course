import urllib.request
from storage import IMAGE_PATH
import requests

IMAGE_URL = "https://picsum.photos/400.jpg"


def download_image() -> None:
    urllib.request.urlretrieve(IMAGE_URL, IMAGE_PATH)


def read_pongs() -> str:
    x = requests.get('http://pingpong-svc/pingpong')
    return x.text
