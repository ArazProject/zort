import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins,İnlineKeyboardButton, İnlineKeyboardMarkup

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token



@client.on_message(filters.command(['start']))
def start(client, message):
    araz = f'`🤔Salam {mention}, Bu bot Araz tərəfindən proqramlaşdırılmış botdur.`**'
    message.reply_text(
        text=araz, 
        quote=False,
        reply_markup=InlineKeyboardMarkup(
            [[
                    InlineKeyboardButton('Rəsmi Kanal ✅', url='https://t.me/extradirda'),
                    InlineKeyboardButton('Support 🎵', url=f'https://t.me/suplegend')
                  ],[
                    InlineKeyboardButton('Developer 👨🏻‍💻', url=f'T.me/Arazdi')
                ]
            ]
        )
    )


print(">> Bot çalıyor merak etme 🚀 @loungesupport bilgi alabilirsin <<")
client.run_until_disconnected()
