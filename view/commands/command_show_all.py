from view.commands.command_abstract import Command


class CommandShowAll(Command):

    @property
    def description(self):
        
        return "Показать все заметки"

    def execute(self):
        
        self.console.show_all()