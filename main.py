import asyncio
from commands import interpreter, system, register_command
import discord
import data

client = data.client


@client.event
async def on_ready():
    print('Bot Successfully Logged in')
    client.loop.create_task(status_task())
    client.loop.create_task(check_should_run_task())
    client.loop.create_task(send_messages_task())


async def send_messages_task():
    while data.should_run:
        liste = []
        for message in data.messages:
            liste.append(message)
        for message in liste:
            data.messages.remove(message)
            if message.embed:
                await message.channel.send(embed=message.content)
            else:
                await message.channel.send(message.content)
        await asyncio.sleep(1)

async def check_should_run_task():
    global client
    while data.should_run:
        await asyncio.sleep(1)
    await asyncio.sleep(3)
    await client.change_presence(activity=discord.Game('Stopping ...'), status=discord.Status.dnd)
    await asyncio.sleep(3)
    await client.logout()


async def status_task():
    while data.should_run:
        await client.change_presence(activity=discord.Game('*help - Flonki Bot'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('Mein DC bot'), status=discord.Status.online)
        await asyncio.sleep(3)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if str(message.content).startswith("*"):
        response = interpreter(message)
        if not response == None:
            if type(response) == discord.Embed:
                await message.channel.send(embed=response)
            else:
                await message.channel.send(response)


with open("token", "r") as file:
    token = file.readline()

register_command(system.HelpCommand())
register_command(system.AnnounceCommand())
register_command(system.StopCommand())

client.run(token)
