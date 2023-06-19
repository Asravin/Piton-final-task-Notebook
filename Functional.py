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




