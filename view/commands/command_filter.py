from view.commands.command_abstract import Command


class CommandFilter(Command):
    
    @property
    def description(self):
        
        return "Сделать выборку заметок по дате"

    def execute(self):
        
        self.console.show_filtered_notebook()