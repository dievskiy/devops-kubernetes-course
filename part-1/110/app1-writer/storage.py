TIMESTAMP_FILE = '/usr/src/app/files/logs.txt'


class FileError(Exception):
    """Error while opening a file"""


def write_timestamp_to_file(timestamp: str) -> None:
    try:
        with open(TIMESTAMP_FILE, 'w') as file:
            file.write(timestamp)
    except OSError:
        raise FileError()
