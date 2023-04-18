from view.commands.command_abstract import Command


class CommandOpen(Command):

    @property
    def description(self):
        
        return "Открыть записную книжку"

    def execute(self):
        
        self.console.open_notebook()