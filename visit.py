
from telethon.tl.types import UpdateShortMessage, ReplyInlineMarkup, KeyboardButtonUrl
from os import environ
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore, init as color_ama
from datetime import datetime
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient, events
import asyncio
import logging
import re
import time
import os
import sys
import requests

logging.basicConfig(level=logging.ERROR)


color_ama(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

# Get your own values from my.telegram.org
api_id = os.environ[api_id]
api_hash = os.environ[api_hash]


doge = 'freecardano_claimbot'


def print_msg_time(message):
    print('[' + Fore.CYAN +
          f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')


def get_response(url, method='GET'):
    response = requests.request(method, url, headers={
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}, timeout=15)
    text_response = response.text
    status_code = response.status_code
    return[status_code, text_response]


async def main():

    print(Fore.MAGENTA + '__      _____ _    ___ ___  __  __ ___ ')
    print(Fore.MAGENTA + '\ \    / / __| |  / __/ _ \|  \/  | __|')
    print(Fore.MAGENTA + ' \ \/\/ /| _|| |_| (_| (_) | |\/| | _| ')
    print(Fore.MAGENTA + '  \_/\_/ |___|____\___\___/|_|  |_|___|\n' + Fore.RESET)
    print(Fore.GREEN + '    -             BY AZZURI             -   \n' + Fore.RESET)

    # Check if phone number is not specified
    if len(sys.argv) < 2:
        print('Usage: python start.py phone_number')
        print('-> Input number in international format (example: +639162995600)\n')
        e = input('Press any key to exit...')
        exit(1)

    phone_number = sys.argv[1]

    if not os.path.exists("session"):
        os.mkdir("session")

    # Connect to client
    client = TelegramClient('session/' + phone_number, api_id, api_hash)
    await client.start(phone_number)
    me = await client.get_me()

    print(f'Current account: {me.first_name}({me.username})\n')
    print_msg_time('Running....')

     # Start command 🎲 Dice
    await client.send_message(doge, '🎲 Dice')
    
    # Print total time
    @client.on(events.NewMessage(chats=doge, incoming=True))
    async def wait_hours(event):
        print_msg_time('Searching')
        message = event.raw_text
        if('Claim your free {} bonus! 🎁') in message:
            await client.send_message(doge, '🎲 Dice')
            print_msg_time('Sending 🎲 Dice command')
        if('🕔 Please Comeback in 30 Minutes!') in message:
                sleep(1920)

    await client.run_until_disconnected()

asyncio.get_event_loop().run_until_complete(main())
