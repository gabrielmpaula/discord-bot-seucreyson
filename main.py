import discord
import json
from bs4 import BeautifulSoup
import requests

def get_patch():
    page = requests.get('https://www.dota2.com/patches/')
    soup = BeautifulSoup(page.text, 'html.parser')
    current_patch = soup.find(class_='PatchTitle').contents[0]
    return current_patch

with open('credentials.json') as f:
    data = json.load(f)

bot_token = data['bot_token']

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = '{0.author.mention} AÍ É JOGADÔ'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!picks'):
        msg = 'https://imgur.com/a/vN4v2aR'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!tier'):
        msg = 'https://imgur.com/DjqZm5p'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!patch'):
        patch = get_patch()
        msg = 'Patch atual: **{}**\nChangelog: https://www.dota2.com/patches/{}'.format(patch, patch)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(bot_token)
