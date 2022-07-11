import os
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
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))
    AUTHORISED_CHAT = [int(i) for i in os.environ.get('AUTHORISED_CHAT').split(" ")]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", 0))
