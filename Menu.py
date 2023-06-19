import Notebook


def input_text(text, n):
    while len(text) <= n:
        print(f"Минимальная длина текста {n} символов\n")
        text = input("Введите текст: ")
    else:
        return text
    

def input(number):
    text = input_text(("Введите название Заголовка: "), number)
    body = input_text(("Введите текст: "), number)
    return Notebook.book(text = text, body = body)

def list_program():
    print("МЕНЮ:\n \n1 - Создать заметку \n2 - Удалить заметку \n3 - Изменить заметку \n4 - Найти заметку по Индексу \n5 - Найти заметку по дате написания" )

