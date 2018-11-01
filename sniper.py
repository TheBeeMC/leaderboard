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
    if message.content.startswith('-leaderbaord'):
            embed = discord.Embed(title="TOP 3 PLAYERS", description="#1      Flam      500", colour=0x1a94f0)
            embed.add_field(name="#2      Enkoder Prime      259", value="#3      Paradise      106", inline=True)
            embed.set_author(name="     Leaderboard", icon_url="")
            embed.set_footer(text="Official Leaderboard")
            await bot.send_message(message.channel, "https://gyazo.com/27ae4b91b635a4569a32d922f5322865")
            await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('-lfeadserbaord'):
            embed = discord.Embed(title="TOP 3 PLAYERS", description="#1      Flam      50", colour=0x1a94f0)
            embed.add_field(name="#2      DrHat      36", value="#3      None", inline=True)
            embed.set_author(name="     Speed Leaderboard", icon_url="")
            embed.set_footer(text="Official Leaderboard")
            await bot.send_message(message.channel, "https://gyazo.com/27ae4b91b635a4569a32d922f5322865")
            await bot.send_message(message.channel, embed=embed)
         
    
             
    if message.content.startswith('!profile'):
        await bot.send_message(message.channel, "Unable to find a tag linked to your discord account. Please save your tag and try it again.")   
      
      
    if message.content.startswith('!save '):
        await bot.send_message(message.channel, "A profile with this hashtag does not exist. Please recheck the provided tag.")            
      
        
    if message.content.startswith('staff'):
        await bot.send_message(message.channel, "If you need help just pm a PCGame Staff and will be on your way.")           
      
       
           
       

@bot.event
async def on_ready():
    await bot.change_status(game=discord.Game(name='Suber Dash Leaderboard'))
    print('sniper.py coded by unpredictable')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
    print('------')

bot.run(os.getenv('TOKEN'))
