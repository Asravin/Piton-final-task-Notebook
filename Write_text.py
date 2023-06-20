import Notebook

def write_text(array, mode):
    text = open("notes.csv", mode = 'w', encoding='utf-8')
    text.seek(0)
    text.close()
    text = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        text.write(Notebook.Note.string_text(notes))
        text.write("\n")
    text.close

    