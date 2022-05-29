LOG_FILE = '/usr/src/app/files/logs.txt'


def read_pongs() -> str:
    try:
        with open(LOG_FILE, 'r') as file:
            return file.readline()
    except OSError:
        raise OSError
