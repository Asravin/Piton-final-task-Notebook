import Notebook

def Write_text(array, mode):
    text = open("notes.csv", mode = "w", encoding = "UTF-8")
    text.seek(0)
    text.close()
    text = open("notes.csv", mode = mode, encoding = "UTF-8")
    for i in array:
        text.write(Notebook.Notebook.string(i))
        text.write("\n")
    text.close