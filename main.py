# This example requires the 'message_content' intent.

import discord
import os
from dotenv import load_dotenv
load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        # メッセージを書いた人がHaruki Inoue以外なら処理終了
        if message.author.id != int(os.environ['USER_ID']):
            return
        channel = message.channel
        await channel.send('Say hello!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run(os.environ['DISCORD_TOKEN'])
