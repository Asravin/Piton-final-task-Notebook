import Notebook
import Menu
import Read_text
import Write_text
number = 6


def note_add():
    note = Menu.input_new(number)
    array = Read_text.read_text()
    for notes in array:
        if Notebook.Note.get_index(note) == Notebook.Note.get_index(notes):
            Notebook.Note.list_index(note)
    array.append(note)
    Write_text.write_text(array, 'a')
    print('Заметка успешно добавлена ')

def searth_note(text):
    boolean = True
    array = Read_text.read_text()
    if text == 'date':
        date = input('Введите дату в формате day.month.year: ')
    for notes in array:
        if text == 'all':
            boolean = False
            print(Notebook.Note.map(notes))
        if text == 'id':
            boolean = False
            print('ID: ' + Notebook.Note.get_index(notes))
        if text == 'date':
            boolean = False
            if date in Notebook.Note.get_date(notes):
                print(Notebook.Note.map(notes))
    if boolean == True:
        print('Заметок не найдено ')

def delete_and_edit(text):
    id = input('Введите индекс заметки: ')
    array = Read_text.read_text()
    boolean = True
    for notes in array:
        if id == Notebook.Note.get_index(notes):
            boolean = False
            if text == 'edit':
                note = Menu.input_new(number)
                Notebook.Note.list_temp(notes, note.get_temp())
                Notebook.Note.list_body(notes, note.get_body())
                Notebook.Note.list_date(notes)
                print('Заметка изменена ')
            if text == 'delete':
                array.remove(notes)
                print('Заметка удалена ')
            if text == 'searth_note':
                print(Notebook.Note.map(notes))
    if boolean == True:
        print('Заметка не найдена ')
    Write_text.write_text(array, 'a')





