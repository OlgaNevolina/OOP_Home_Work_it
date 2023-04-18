from datetime import datetime


class Note:

    def __init__(self, title, creation_data, text_note, changes_data=''):
        self.__title = title
        self.__text_note = text_note
        self.__creation_data = creation_data
        self.__changes_data = changes_data

    def get_title(self):
        
        return self.__title

    def get_creation_data(self):
        
        return self.__creation_data

    def get_changes_data(self):
        
        return self.__changes_data

    def get_text_note(self):
        
        return self.__text_note

    def change(self, title: str, new_text: str):
        
        if title:
            self.__title = title
        if new_text:
            self.__text_note = new_text
        self.__changes_data = datetime.today().strftime('%d.%m.%Y %H:%M')