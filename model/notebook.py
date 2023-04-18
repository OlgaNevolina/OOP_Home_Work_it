from datetime import datetime
from tabulate import tabulate


from model.note import Note


class Notebook:

    def __init__(self):
        self.__notes = []

    def size(self):
        
        return len(self.__notes)

    def add_note(self, title, text_note):
        
        note = Note(title, datetime.today().strftime('%d.%m.%Y %H:%M'), text_note)
        self.__notes.append(note)

    def remove_note(self, index):
        
        del self.__notes[index]

    def change_note(self, index, title, update_text):
        
        self.__notes[index].change(title, update_text)

    def is_full(self):
        
        return bool(self.__notes)

    def get_notes(self):
        
        return self.__notes

    @property
    def tabl(self):
        
        headers = ['№', 'Заголовок', 'Заметка', 'Дата/время создания', 'Дата/время изменения']
        tabl = [[i, note.get_title(), note.get_text_note(),
                 note.get_creation_data(), note.get_changes_data()]
                for i, note in enumerate(self.__notes, start=1)]
        return tabulate(tabl, headers=headers, tablefmt="fancy_grid", stralign='center')

    def filter_by_date(self, date):
        
        headers = ['№', 'Заголовок', 'Заметка', 'Дата/время создания', 'Дата/время изменения']
        tabl = [[i, note.get_title(), note.get_text_note(), note.get_creation_data(),
                 note.get_changes_data()] for i, note in enumerate(self.__notes, start=1)
                if date in note.get_creation_data() or date in note.get_changes_data()]
        return tabulate(tabl, headers=headers, tablefmt="fancy_grid", stralign='center')