from telethon import TelegramClient, types, events
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']


client = TelegramClient('mzmograbber', api_id, api_hash)
client.start()

print('STARTED')  # LOGGING HERE IF NEEDED

@client.on(events.NewMessage(chats=[-1001125494101]))
async def normal_handler(event):
    # username = '@' + str(event.chat.username)
    if 'pushkino' in str(event.message).lower():
        if isinstance(event.chat, types.Channel):
            await client.send_message(-100236842683, event.message)
            print(event.message)
client.run_until_disconnected()