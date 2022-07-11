from pyrogram.client import Client
from pyrogram import enums, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import LOGGER, AUTHORISED_USERS, OWNER_ID


@Client.on_message(filters.command('start'))
async def start(bot, message):
    LOGGER.info('UID: {} - UN: {} - MSG: {}'.format(message.chat.id,
                message.from_user.mention, message.text))
    if message.chat.id in AUTHORISED_USERS or message.from_user.id == OWNER_ID:
        start_string = f'''Hello {message.from_user.mention} I am PyroBot'''
        await message.reply_text(start_string, reply_markup=START_BUTTONS)
    else:
        await message.reply_text('''Oops You are not authorized''')


START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)


@Client.on_message(filters.command('help') & (filters.chat(AUTHORISED_USERS) | filters.user(OWNER_ID)))  # noqa
async def help(bot, message):
    await message.reply_text(HELP_TEXT, disable_web_page_preview=True,
                             parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query()
async def cb_handler(bot, message):
    if message.data == "help":
        await message.message.edit_text(
            text=HELP_TEXT,
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )

    elif message.data == "close":
        await message.message.delete()


HELP_TEXT = """SAMPLE HELP TEXT"""
