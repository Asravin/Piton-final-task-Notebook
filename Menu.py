import Notebook

def input_text(text, num):
    while len(text) <= num:
        print(f"Минимальная длина текста {num} символов\n")
        text = input("Введите текст: ")
    else:
        return text
    

def input(num):
    text = input_text(("Введите название Заголовка: "), num)
    body = input_text(("Введите текст: "), num)
    return Notebook.Notebook(text = text, body = body)

def list_program():
    print("МЕНЮ:\n \n1 - Создать заметку \n2 - Удалить заметку")

