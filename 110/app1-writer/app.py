#!/usr/bin/env python3.10

# This app generates a new timestamp every 5 seconds and saves it into a file /usr/src/app/files/logs.txt
from time import sleep
from timestamp import generate_timestamp
from storage import write_timestamp_to_file, FileError

SLEEP_TIME_SECONDS = 5


def main() -> None:
    while True:
        timestamp = generate_timestamp()
        try:
            write_timestamp_to_file(timestamp)
        except FileError as err:
            print(str(err))
        sleep(SLEEP_TIME_SECONDS)


main()
