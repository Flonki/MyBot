import asyncio
from commands import interpreter, system, register_command
import discord
import data
import sys
import time

client = discord.Client()


@client.event
async def on_ready():
    print('Bot Successfully Logged in')
    client.loop.create_task(status_task())
    client.loop.create_task(check_should_run_task())


async def check_should_run_task():
    global client
    while data.should_run:
        await asyncio.sleep(1)
    await asyncio.sleep(3)
    await client.change_presence(activity=discord.Game('Stopping ...'), status=discord.Status.online)
    await asyncio.sleep(3)
    await client.logout()


async def status_task():
    while data.should_run:
        await client.change_presence(activity=discord.Game('*help - Flonki MC Bot'), status=discord.Status.online)
        await asyncio.sleep(3)
        if data.should_run:
            await client.change_presence(activity=discord.Game('Mein DC bot'), status=discord.Status.online)
            await asyncio.sleep(3)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if str(message.content).startswith("*"):
        response = interpreter(message)
        if not response == None:
            await message.channel.send(response)


with open("token", "r") as file:
    token = file.readline()

register_command(system.HelpCommand())
register_command(system.IpCommand())
register_command(system.StopCommand())

client.run(token)
