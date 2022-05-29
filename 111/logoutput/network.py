import urllib.request
from storage import IMAGE_PATH

IMAGE_URL = "https://picsum.photos/400.jpg"


def download_image() -> None:
    urllib.request.urlretrieve(IMAGE_URL, IMAGE_PATH)
