from view.commands.command_abstract import Command


class CommandSave(Command):

    @property
    def description(self):
        
        return "Сохранить изменения"

    def execute(self):
        
        self.console.save_changes()