from commands import Command
from commands import commands

import data


class HelpCommand(Command):
    def __init__(self):
        super().__init__("help", "Zeigt Hilfe an.")
        self.message = None
        self.longestcommand = 0

    def run(self, args, user):
        if self.message == None:
            self.message = "Commands:"
            for command in commands:
                if self.longestcommand <= len(command.commandname):
                    self.longestcommand = len(command.commandname)

            for command in commands:
                space = ((self.longestcommand + 2) - len(command.commandname)) * " "
                self.message = self.message + "\n " + command.commandname + space + " - " + command.description

        return self.message


class StopCommand(Command):
    def __init__(self):
        super().__init__("stop", "Stoppt den Bot")

    def run(self, args, user):

        for role in user.roles:
            if role.id == 717753987578986526:
                data.should_run = False
                return "Der Bot wird nun gestoppt. Von: " + user.display_name

        return "Du hast nicht die Rechte für diesen Befehl"


class IpCommand(Command):
    def __init__(self):
        super().__init__("ip", "Zeigt die Server IP")




