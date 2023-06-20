import Notebook

def read_text():
    try:
        array = []
        text = open("notes.csv", "r", encoding = 'utf-8')
        notes = text.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Notebook.Note(
                id = split_n[0], temp = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print("Заметок пока не создано ")
    finally:
        return array