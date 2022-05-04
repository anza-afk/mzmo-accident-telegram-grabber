from telethon import TelegramClient, types, events
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

client = TelegramClient('mzmo-grabber', api_id, api_hash)
client.start()

print('STARTED')  # LOGGING HERE IF NEEDED

@client.on(events.NewMessage(chats=[-1001125494101, '@Ondor']))
async def normal_handler(event):
    if 'pushkino' in str(event.message).lower():
        await client.send_message(entity=-1001606300804, message=event.message)
        print(event.message)
client.run_until_disconnected()