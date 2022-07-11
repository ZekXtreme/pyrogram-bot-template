from pyrogram.client import Client
from pyrogram import __version__
from pyrogram.types import BotCommand
from pyrogram.raw.all import layer
from . import LOGGER, Config

plugins = dict(
    root="bot/modules"
)

botcmds = [
    BotCommand('start', 'Check Bot is alive'),
    BotCommand('log', 'Send Bot logs'),
    BotCommand('help', 'Send Help Message')
]


class Bot(Client):
    def __init__(self):
        super().__init__(
            "pyrobot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=plugins
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        un = '@' + me.username
        await self.send_message(chat_id=Config.LOG_CHANNEL, text="**Bot Started**")
        await self.set_bot_commands(botcmds)
        LOGGER.info(
            f"Pyrogram v{__version__} (Layer {layer}) started on {un}.")

    async def stop(self, *args):
        await self.delete_bot_commands()
        await super().stop()
        LOGGER.info('Bot Stopped!')


if __name__ == "__main__":
    app = Bot()
    app.run()
