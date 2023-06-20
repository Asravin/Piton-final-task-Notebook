from datetime import datetime
import uuid

class Note:
    def __init__(self,  id = str(uuid.uuid1())[0:2],  temp = "текст", body = "текст", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.temp = temp
        self.body = body
        self.date = date
    
    def get_index(note):
        return note.id
    
    def get_temp(note):
        return note.temp
    
    def get_body(note):
        return note.body
    
    def get_date(note):
        return note.date
    
    def list_index(note):
        note.id = str(uuid.uuid1())[0:2]

    def list_temp(note, temp):
        note.temp = temp
    
    def list_body(note, body):
        note.body = body

    def list_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    
    def string_text(note):
        return note.id + ';' + note.temp + ';' + note.body + ';' + note.date

    def map(note):
        return '\nID: ' + note.id + '\n' + 'Заголовок' + note.temp + '\n' + 'Текст заметки' + '\n' + note.body + '\n' + 'Дата' + note.date