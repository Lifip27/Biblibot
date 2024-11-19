import discord
from discord.ext import commands
from requests import getverse
import numpy as np
with open("token.txt", "r") as f:
    DISCORD_TOKEN = f.read()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command(name='verse')
async def verse(ctx, *args):
    if len(args) == 0:
        await ctx.send("Please enter a book.")
        return
    book = args[0]
    if len(args) == 2:
        
        if len(args[1].split(":")) == 1:
            chap = getverse(book, args[1].split(":")[0], "*")
            # print(len(chap)//2)
            formatchap = np.array_split(chap, 5)
            for i in formatchap:
                await ctx.send(f"**{str(i)[1:-1]}** ||{ctx.author.mention}||")
            return
                
        chapter, verse = args[1].split(":")
        if "-" not in verse:
            await ctx.send(f'**{getverse(book, chapter, verse)}** \n||{ctx.author.mention}||')
            return
        else:
            start, end = verse.split("-")
            message = ''
            for i in range(int(start), int(end)+1):
                message+=f'{getverse(book, chapter, i)}\n'
            await ctx.send(f'**{message}** \n||{ctx.author.mention}||')
    if len(args) == 1:
        await ctx.send(getverse(book, 1, 1))
        
    
         
    
    

bot.run(DISCORD_TOKEN)