import Notebook
import Menu
import Read_text
import Write_text
number = 4


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



