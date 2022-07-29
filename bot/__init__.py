from contextlib import suppress
import os
from sys import exit
import logging
from dotenv import load_dotenv


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(
        'log.txt'), logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

if os.path.exists('config.env'):
    load_dotenv('config.env')


class Config(object):
    try:
        API_ID = int(os.environ.get("API_ID"))
        API_HASH = os.environ.get("API_HASH")
        BOT_TOKEN = os.environ.get("BOT_TOKEN")
        OWNER_ID = int(os.environ.get("OWNER_ID", 0))
    except BaseException:
        logging.error("One or more env variables missing! Exiting now")
        exit(1)
    with suppress(Exception):
        LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", 0))
        AUTHORISED_CHATS = [int(i) for i in os.environ.get('AUTHORISED_CHAT').split(" ")]
