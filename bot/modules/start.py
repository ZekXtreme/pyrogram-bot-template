from pyrogram.client import Client
from pyrogram import enums, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from bot import LOGGER, Config


AUTHORISED_CHATS = Config.AUTHORISED_CHATS
OWNER_ID = Config.OWNER_ID


@Client.on_message(filters.command('start'))
async def start(_, message: Message):
    LOGGER.info(f'UID: {message.chat.id,} - UN: {message.from_user.mention} - MSG: { message.text}')
    if message.chat.id in AUTHORISED_CHATS or message.from_user.id == OWNER_ID:
        start_string = f'''Hello {message.from_user.mention} I am PyroBot'''
        await message.reply_text(start_string, reply_markup=START_BUTTONS)
    else:
        await message.reply_text("Not a authorized user")


START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)


@Client.on_message(filters.command('help') & (filters.chat(AUTHORISED_CHATS) | filters.user(OWNER_ID)))  # noqa
async def help(_, message: Message):
    await message.reply_text(HELP_TEXT, disable_web_page_preview=True,
                             parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query()
async def cb_handler(_, query: CallbackQuery):
    if query.data == "help":
        await query.message.edit_text(
            text=HELP_TEXT,
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True
        )

    elif query.data == "close":
        await query.message.delete()


HELP_TEXT = """SAMPLE HELP TEXT"""
