import os
from nats.aio.client import Client as NATS
import nats

URL = os.getenv('NATS_URL')
if not URL:
    """
    Fail if env is not provided
    """
    raise ValueError("NATS_URL was not specified")


async def publish_todo(todo: str, status: str) -> bool:
    """
    Publish a todo to the todos subscription
    :param todo: todo to publish
    :return: True if published successfully
    """
    nc = NATS()
    try:
        await nc.connect(URL, max_reconnect_attempts=-1)
        await nc.publish('todos', f'{todo}: current status is <b>{status}</b>'.encode('ascii'))
    except Error as err:
        print(f'Error: publish_todo: {err}')
        return False
    return True
