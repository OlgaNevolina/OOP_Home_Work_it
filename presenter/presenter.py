from model.file_reader import FileReader


class Presenter:

    def __init__(self, view, notebook, path):
        self.__view = view
        self.__notebook = notebook
        self.__view.set_presenter(self)
        self.file = FileReader(path)

    def open_file(self):
        
        self.__notebook = self.file.file_read(self.__notebook)

    def save(self):
        
        self.file.save_changes(self.__notebook)

    def is_full(self):
        
        return self.__notebook.is_full()

    def add_note(self, title_text, text_note):
        
        self.__notebook.add_note(title_text, text_note)

    def remove_note(self, index):
        
        self.__notebook.remove_note(index)

    def change_note(self, index, update_title, update_text):
        
        self.__notebook.change_note(index, update_title, update_text)

    def get_size_notebook(self):
        
        return self.__notebook.size()

    def get_tabl_notebook(self):
        
        return self.__notebook.tabl

    def get_filtered_tabl(self, date):
        
        return self.__notebook.filter_by_date(date)