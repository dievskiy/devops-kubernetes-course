#!/usr/bin/env python3

import time
import uuid
import datetime


def generate_random_string() -> str:
    """
    Generates random string
    """
    return str(uuid.uuid4())


if __name__ == "__main__":
    while True:
      print(f"{datetime.datetime.now()}: {generate_random_string()}")
      time.sleep(5)
    
