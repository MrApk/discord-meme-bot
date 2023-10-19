import random
import discord
import requests

MyClient = discord.Client
intents = discord.Intents.default()
intents.message_content = True
bot = MyClient(intents=intents)


@bot.event
async def on_message(message):
  if message.content.startswith('?meme'):
    # Get a random meme from the API
    response = requests.get('https://api.popcat.xyz/meme')
    meme = response.json()
    em = discord.Embed(title=meme['title'],description=None,colour=random.randint(0, 0xFFFFFF),url=meme['url'])
    em.set_image(url=meme['image'])

    # Send the meme to the channel
    await message.channel.send(embed=em)
    print('done meme')

@bot.event
async def on_ready():
  print('Connected to bot: {}'.format(bot.user.name))
  print('Bot ID: {}'.format(bot.user.id))
  print('Your bot is online!✅')


bot.run('Token')

#Make By APK
