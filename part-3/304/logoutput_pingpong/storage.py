import base64
from os.path import exists

LOG_PATH = '/usr/src/app/files/logs.txt'
IMAGE_PATH = '/usr/src/app/files/image.jpg'


def is_image_present() -> bool:
    return exists(IMAGE_PATH)


def read_image() -> bytes:
    with open(IMAGE_PATH, 'rb') as image:
        return base64.b64encode(image.read())


def read_pongs() -> str:
    try:
        with open(LOG_PATH, 'r') as file:
            return file.readline()
    except OSError:
        raise OSError
