import requests
import os

CHAT_ID = os.getenv('CHAT_ID')
TOKEN = os.getenv('TG_TOKEN')

print(f"TOKEN is {TOKEN}, CHAT_ID is {CHAT_ID}")

if not CHAT_ID or not TOKEN:
    raise ValueError("Char ID or TOKEN was not specified")

TOKEN = TOKEN.replace("\n", "")


async def send_message(data: str):
    """
    Send data to the telegrame bot
    :param data: Data to send
    :return: True if sent successfully
    """
    send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' \
                + CHAT_ID + '&parse_mode=Markdown&text=' + data
    print(f"Send text was {send_text}")
    response = requests.get(send_text)
    return response.ok
