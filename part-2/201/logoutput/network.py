import requests


def read_pongs() -> str:
    x = requests.get('http://pingpong-v3-svc:1111/pingpong')
    return x.text
