from datetime import datetime
import uuid

class Notebook:
    def initialization(book, index = str(uuid.uuid1())[0:3], text = "текст", body = "текст", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        book.index = index
        book.text = text
        book.body = body
        book.date = date
    
    def get_index(note):
        return note.index
    
    def get_text(note):
        return note.text
    
    def get_body(note):
        return note.body
    
    def get_date(note):
        return note.date
    
    def list_index(note):
        note.index = str(uuid.uuid1())[0:3]

    def list_text(note, text):
        note.text = text
    
    def list_body(note, body):
        note.body = body

    def list_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    
    def string(note):
        return note.index + note.text + note.body + note.date

    def map(note):
        return "\n Index: " + note.index + "\n" + "Заголовок" + note.text + "\n" + "Текст заметки" + "\n" + note.body + "\n" + "Дата" + note.date