import Notebook
import Menu
import Read_text
import Write_text
number = 5


def note_add():
    note = Menu.input_text(number)
    arr = Read_text.read_text()
    for notes in arr:
        if Notebook.book.get_index(note) == Notebook.book.get_index(notes):
            Notebook.book.list_index(note)
    arr.append(note)
    Write_text.write_text(arr, "a")
    print("Заметка успешно добавлена ")

def searth_note(text):
    boolean = True
    arr = Read_text.read_text()
    if text == "date":
        date = input("Введите дату в формате day.month.year: ")
        for notes in arr:
            if text == "all":
                boolean = False
                print(Notebook.book.map(notes))
            if text == "index":
                boolean = False
                print("Index: " + Notebook.book.get_index(notes))
            if text == "date":
                boolean = False
                if date in Notebook.book.get_date(notes):
                    print(Notebook.book.map(notes))
    if boolean == True:
        print("Заметок не найдено ")

def delete_and_edit(text):
    index = input("Введите индекс заметки: ")
    arr = Read_text.read_text()
    boolean = True
    for notes in arr:
        if index == Notebook.book.get_index() :
            boolean = False
            if text == "edit":
                note = Menu.input_text(number)
                Notebook.book.list_text(notes, note.get_text())
                Notebook.book.list_body(notes, note.get_body())
                Notebook.book.list_date(notes)
                print("Заметка изменена ")
            if text == "delete":
                arr.remove(notes)
                print("Заметка удалена ")
            if text == "searth_note":
                print(Notebook.book.map(notes))
    if boolean == True:
        print("Заметка не найдена ")
    Write_text.write_text(arr, "a")




