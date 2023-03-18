# This example requires the 'message_content' intent.

# keep_aliveは本番環境で実行するときのみ必要？
# from keep_alive import keep_alive
import discord
import os
from dotenv import load_dotenv
load_dotenv()
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        # メッセージを書いた人がBotなら処理終了
        if message.author.bot:
        # if message.author.id != int(os.environ['MY_USER_ID']): #自分で確認する用
            return
        channel = message.channel 
        # topic = '起きた' #反応する文字列
        # text = 'おはよう' #返信する文字列
        if message.content == '起きた':
            await channel.send('おはよう')
        if '終わった' in message.content or 'おわった' in message.content or '疲れた' in message.content or 'つかれた' in message.content:
            await channel.send('お疲れ様')
        if 'ありがとう' in message.content:
            await channel.send('どういたしまして')
        if '見た' in message.content or 'みた' in message.content:
            await channel.send('なに見てんだ')
       
        erai_reply = [
            'えらい',
            '普通かな',
            'エラーイ',
            'できて当然じゃない？'
        ]
        yabai_message_reply = [
            '通常運転',
            '今日も元気ですね'
        ]
        #メッセージ送信者が自分の場合
        if message.author.id == int(os.environ['MY_USER_ID']):
            if 'えらい' in message.content or '偉い' in message.content:
                await channel.send('えらい！！！')
        #メッセージ送信者が特定のUSER_IDの場合
        if message.author.id == int(os.environ['USER_ID']):
            if 'すだっち' in message.content and ('えらい'in message.content or '偉い'in message.content):
                await channel.send('えらい！！！')
            if '私' in message.content and ('えらい'in message.content or '偉い'in message.content):
                await channel.send(random.choice(erai_reply))

        #特定のチャンネルにメッセージが送信された場合のみBotが返事を返す
        if channel.id == int(os.environ['YABAI_CHANNEL_ID']):
            await channel.send(random.choice(yabai_message_reply))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
# keep_alive()
client.run(os.environ['DISCORD_TOKEN'])
