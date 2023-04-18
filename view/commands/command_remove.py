from view.commands.command_abstract import Command


class CommandRemove(Command):

    @property
    def description(self):
        
        return "Удалить заметку"

    def execute(self):
        
        self.console.remove_note()