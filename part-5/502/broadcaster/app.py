import asyncio
from nats.aio.client import Client as NATS
from send import send_message
import nats
import os

URL = os.getenv('NATS_URL', 'nats://my-nats:4222')


async def run():
    nc = NATS()

    await nc.connect(URL, max_reconnect_attempts=-1)

    async def todos_request(msg):
        subject = msg.subject
        reply = msg.reply
        data = msg.data.decode()
        print("Received a message on '{subject} {reply}': {data}"
              .format(subject=subject, reply=reply, data=data))
        if not reply:
            await send_message(data)
        await nc.publish(reply, b'worker_up')

    await nc.subscribe("todos", "broadcast_workers", todos_request)

    for _ in range(1, 1000000):
        await asyncio.sleep(1)
        try:
            response = await nc.request("todos", b'awake_workers')
            print(response)
        except Exception as e:
            print("Error:", e)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.run_forever()
    loop.close()
