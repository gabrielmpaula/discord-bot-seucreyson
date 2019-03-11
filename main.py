import discord

import json

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
        msg = 'https://imgur.com/a/i4Ru5m9'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!tier'):
        msg = 'https://imgur.com/DjqZm5p'
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(bot_token)