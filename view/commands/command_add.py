from view.commands.command_abstract import Command


class CommandAdd(Command):

    @property
    def description(self):
        
        return "Добавить заметку"

    def execute(self):
        
        self.console.add_note()