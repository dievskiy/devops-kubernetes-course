TIMESTAMP_FILE = '/usr/src/app/files/logs.txt'


class FileError(Exception):
    """Error while opening a file"""


def read_timestamp_from_file() -> str:
    """Reads the last line of file"""
    try:
        with open(TIMESTAMP_FILE, 'r') as file:
            return file.readline()
    except OSError:
        raise FileError()
