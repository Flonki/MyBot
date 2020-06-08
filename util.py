import discord


class Message:
    def __init__(self,message,channel:discord.TextChannel):
        self.embed = False
        self.channel = channel
        if type(message) == discord.Embed:
            self.embed = True
        self.content = message