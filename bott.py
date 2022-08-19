# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import datetime
from discord.ext import commands, tasks
import requests
from bs4 import BeautifulSoup
import random
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()
bot = commands.Bot(command_prefix='.')

global counter
counter = 0






def validateNumArgs(args, num):
	if(len(args) == num):
		return True

	else:
		return False



# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	counter = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	args = message.content.split()
	if(not message.author.bot):
		print(message.author.name)
		print(message.content)
	
	# if(message.author.name == "Christofu"):
	# 	await message.reply("Chris sthu")

	if message.content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		global counter
		counter += 1

		print(counter)
		#await message.channel.send("ur cringe")
		await message.reply("ur cringe")

	elif (args[0] == "add"):
		if(not validateNumArgs(args, 3)): 
			await message.reply("not correct number of args")
		
		else:
			await message.reply(int(args[1]) + int(args[2]))
	
@bot.command
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("I am terribly sorry, but I cannot join you as you are not in a voice channel.")


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(token)


