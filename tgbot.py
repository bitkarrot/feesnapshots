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


@events.register(events.NewMessage(incoming=True, outgoing=False))
async def handler(event):
    input = str(event.raw_text)
    sender = await event.get_sender()
    username = sender.username
    rawtext = event.raw_text
    print(rawtext)
    chat = await event.get_chat()
    # print(f'chat: {chat}')
    me = await client.get_me()
    chat_id = event.chat_id
    print(f'chatid: {chat_id}')
    
    if '/test' in rawtext:
        
        # this message goes to the group if called in group
        # or to the sender if called by sender 
        await event.reply(" ok fetching... give me a moment" )
        
        # use chat_id to send to sender in DM, or group, 
        # wherever the event originated
        wtfmsg = ["<b> whatthefee.io by Felix Weis. </b>\n"
                "x-axis: confirmation probability,\n", 
                "y-axis: maximum confirmation time \n", 
                "cell value: sats per bit(pure mining fee)\n"]
        
        await client.send_message(chat_id, ''.join(wtfmsg))
        await client.send_file(chat_id, './images/wtf.png')
    
        notify = "Please Note: Images updated hourly, not in real time\n"
        await client.send_message(chat_id, notify)

client.start(bot_token=TOKEN)

with client:
    client.add_event_handler(handler)
    logger.info('(Press Ctrl+C to stop this) tg bot')
    client.run_until_disconnected()
