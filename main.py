# Konzept Discord Chatbot
# 1. Chatbot greets user
# 2. Chatbot tells user that he can ask him anything regarding geography (or something like that.)
# 3. User asks a question
# 4. Chatbot answers questions
# 5. Optional: User can win points for every right question
# 6 Optional: Bot saves result in array, outputs a ranking if asked by the user.

# Import Modules
import asyncio
from http import client
import os
from random import random
import discord
from dotenv import load_dotenv



# Start Chatbot
intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} ist online!")
    channel = client.get_channel(os.getenv("CHANNEL"))
    await channel.send("Hallo Leute, ich bin erwacht!")


# First default bot response
@client.event
async def on_message(msg):
    if msg.author.bot:
        return

    await msg.channel.send(
        "Hey, na wie gehts? Ich weiß ziemlich viel. Stell mir eine Frage zum Thema Geografie."
    )

# Automatic Delete Notification
@client.event
async def on_message_delete(msg):
    await msg.channel.send(f"Eine Nachricht von {msg.author} wurde gelöscht: {msg.content}")


## Get Discord token from .env-file and start bot
load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))