import discord
from discord.ext import commands
from requests import getverse

with open("token.txt", "r") as f:
    DISCORD_TOKEN = f.read()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(message.content)
    print(message.author)
    if message.content.startswith("?"):
        try:
            print('E')
            default = message.content.split(" ")[0]
            if default == "?verse":
                book = message.content.split(" ")[1]
                if book == "list":
                    reply = "Here are the books of the Bible:"
                    await message.channel.send(reply)
                    reply = getverse(book, None, None)
                    await message.channel.send(f"{reply} {message.author.mention}")
                    return
                if (len(message.content.split()) > 2):
                    chapter = message.content.split(" ")[2]
                    verse = message.content.split(" ")[3]
                    reply = getverse(book, chapter, verse)
                    await message.channel.send(f"{reply} {message.author.mention}")
                    return
                else:
                    reply = getverse(book, 1, 1)
                    await message.channel.send(f"{reply} {message.author.mention}")
                    return
        except Exception as e:
            print(e)

bot.run(DISCORD_TOKEN)