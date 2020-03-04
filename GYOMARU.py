# -*- coding:utf-8 -*-

import discord, asyncio

token = "NjgyMTg4NzUwNDIzMzI2NzQw.XlnqiA.OShcs1GbpPwdOPcnfaec9GOggus"
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("반갑습니다 :D"))
    print("I'm Ready!")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot:
        return none

    if message.content == "!안녕":
        await message.channel.send("반가워요")
        await message.author.send("사실 난 여기있다구")

client.run(NjgyMTg4NzUwNDIzMzI2NzQw.XlnqiA.OShcs1GbpPwdOPcnfaec9GOggus)