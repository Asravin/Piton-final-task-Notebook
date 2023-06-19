import Notebook

def Write_text(array, mode):
    text = open("notes.csv", mode = "w", encoding = "UTF-8")
    text.seek(0)
    text.close()
    text = open("notes.csv", mode = mode, encoding = "UTF-8")
    for note in array:
        text.write(Notebook.Notebook.string(note))
        text.write("\n")
    text.close