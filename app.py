from telethon import TelegramClient, events
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
entity = eval(config['Telegram']['entity'])
chats = eval(config['Telegram']['chats'])

with open('vlans.txt', 'r', encoding='utf-8') as vlans:
    vlan_dict = [eval(line) for line in vlans]

client = TelegramClient('mzmo-grabber', api_id, api_hash)
client.start()

print('STARTED', chats)  # ADD LOGGING HERE IF NEEDED

@client.on(events.NewMessage(chats=chats))
async def normal_handler(event):
    grabbed_string = str(event.message.message)
    if 'pushkino' in grabbed_string or 'ivanteevka' in grabbed_string:
        for vlan, lpu in vlan_dict:
            if vlan in grabbed_string.lower():
                grabbed_vlan = lpu
        try:
            grabbed_string = f'Achtung!!!\n\n{grabbed_vlan}\n\n{grabbed_string}'
        except UnboundLocalError:
            grabbed_string = f'Achtung!!!\n\nvlan не найден!\n\n{grabbed_string}'
        await client.send_message(entity=entity, message=grabbed_string)
        print(grabbed_string)
client.run_until_disconnected()