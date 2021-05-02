from telethon import TelegramClient, events, Button
import yaml
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('telethon').setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)

path  = "./"
config_file = path + 'config.yml'
with open(config_file, 'rb') as f:
    config = yaml.safe_load(f)
f.close()


client = TelegramClient(config["session_name"],
                        config["api_id"],
                        config["api_hash"])


TOKEN = config['bot_token']
logger.info(f'Bot Token: {TOKEN}')

# Default to another parse mode
client.parse_mode = 'html'


@client.on(events.NewMessage(pattern='(?i)/start', forwards=False, outgoing=False))
async def new_handler(event):
    await event.reply('Hi! Go to /help for instructions')

import os
from datetime import datetime
import time

@events.register(events.NewMessage(incoming=True, outgoing=False))
async def handler(event):

    rawtext = event.raw_text
    chat_id = event.chat_id
    # print(f'chatid: {chat_id}')
    
    if '/test' in rawtext:
        
        wtf_path = './images/wtf.png'
        
        if not os.path.exists(wtf_path):
            print(f'path does not exist: {wtf_path}')
            return

        # this message gets sent first as the rest takes a while
        await event.reply(" ok fetching... give me a moment" )

        # use chat_id to send to sender in DM, or group,
        # wherever the event originated
        wtfmsg = ["<b> whatthefee.io by Felix Weis. </b>\n"
                "x-axis: <b> confirmation probability, </b>\n", 
                "y-axis: <b> max confirmation time </b> \n", 
                "cell value: sats per bit (mining fee)\n"]
        
        lastmodified= datetime.fromtimestamp(os.stat(wtf_path).st_mtime)
        lastmod = str(lastmodified).split(".")[0]
        await client.send_message(chat_id, ''.join(wtfmsg))
        await client.send_file(chat_id, wtf_path)
        curr = str(datetime.fromtimestamp(time.time())).split(".")[0]
        notify = f"Images updated hourly.\n<b>Last updated:</b> {lastmod}\n<b>Current Time:</b> {curr}"
        await client.send_message(chat_id, notify)

client.start(bot_token=TOKEN)

with client:
    client.add_event_handler(handler)
    logger.info('(Press Ctrl+C to stop this) tg bot')
    client.run_until_disconnected()
