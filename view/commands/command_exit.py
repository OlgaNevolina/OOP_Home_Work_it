from view.commands.command_abstract import Command


class CommandExit(Command):

    @property
    def description(self):
        
        return "Завершить работу"

    def execute(self):
        
        self.console.finish()