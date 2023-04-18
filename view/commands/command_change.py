from view.commands.command_abstract import Command


class CommandChange(Command):

    @property
    def description(self):
        
        return "Изменить заметку"

    def execute(self):
        
        self.console.change_note()