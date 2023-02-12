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

        # メッセージを書いた人がHaruki InoueのUSER_ID以外なら処理終了
        if message.author.id != int(os.environ['USER_ID']):
            return
        channel = message.channel 
        topic = '起きた' #反応する文字列
        text = 'おはよう' #返信する文字列
        if message.content == topic:
            await channel.send(text)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run(os.environ['DISCORD_TOKEN'])
