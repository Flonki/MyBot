from discord.message import Message,Member


commands = []


class Command:
    def __init__(self, commandname, description):
        self.commandname = commandname
        self.description = description

    def run(self, message:Message,args):
        pass


def register_command(command):
    global commands
    commands.append(command)


def interpreter(message: Message) -> str:
    global commands

    args = list(str(message.content).split(" "))
    executed_command = args[0].replace("*", "", 1)

    response = "Befehl nicht gefunden."

    if not message.channel.id == 719173290010214412:
        return None

    for command in commands:
        if command.commandname == executed_command:
            response = command.run(message=message,args=args)

    return response
