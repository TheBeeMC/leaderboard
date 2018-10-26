# sniper.py
import discord
from discord.ext import commands
import random
import asyncio
import os
import subprocess
import logging

command_prefix='+'
bot = commands.Bot(command_prefix)
description = 'sniper.py, coded by unpredictable'
 
@bot.event
async def on_message(message):
    if message.content.startswith('+listlead'):
            embed = discord.Embed(title="What is your highest score?", description="Posted on Sunday, October 21, 2018", colour=0x1a94f0)
            embed.add_field(name="First Place with 500 Points: Commit", value="2nd Place with 374 Points: PCGame & 3rd Place with 106 Points: Paradise", inline=True)
            embed.set_author(name="Current Leaderboard Status", icon_url="")
            embed.set_footer(text="Official Leaderboard Status")
            await bot.send_message(message.channel, "https://i.gifer.com/JG3c.gif")
            await bot.send_message(message.channel, embed=embed)

         
    
             
    if message.content.startswith('!profile'):
        await bot.send_message(message.channel, "Unable to find a tag linked to your discord account. Please save your tag and try it again.")   
      
      
    if message.content.startswith('!save '):
        await bot.send_message(message.channel, "A profile with this hashtag does not exist. Please recheck the provided tag.")            
      
        
    if message.content.startswith('staff'):
        await bot.send_message(message.channel, "If you need help just pm a PCGame Staff and will be on your way.")           
      
       
           
       

@bot.event
async def on_ready():
    await bot.change_status(game=discord.Game(name=''))
    print('sniper.py coded by unpredictable')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
    print('------')

bot.run(os.getenv('TOKEN'))
