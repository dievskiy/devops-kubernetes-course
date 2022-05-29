LOG_FILE = '/usr/src/app/files/logs.txt'


def write_to_file(pongs: int) -> None:
    try:
        with open(LOG_FILE, 'w') as file:
            file.write(str(pongs))
    except OSError:
        raise OSError
