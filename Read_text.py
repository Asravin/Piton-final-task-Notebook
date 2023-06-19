import Notebook

def Read_text():
    try:
        array = []
        text = open("notes.csv", "r", encoding = "UTF-8")
        notes = text.read().strip().split("\n")
        for i in notes:
            split_i = i.split(";")
            note = Notebook.Notebook(index = split_i[0], text = split_i[1], body = split_i[2], date = split_i[3])
            array.append(note)
    except Exception:
        print("Заметок пока не создано ")
    finally:
        return array