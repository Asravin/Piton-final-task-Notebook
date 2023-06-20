import Notebook

def input_new(number):
    temp = input_text(
        input('Введите название Заголовка: '), number)
    body = input_text(
        input('Введите текст: '), number)
    return Notebook.Note(temp=temp, body=body)

def input_text(text, n):
    while len(text) <= n:
        print(f"Минимальная длина текста {n} символов\n")
        text = input("Введите текст: ")
    else:
        return text

def list_program():
    print("\n МЕНЮ:\n\n1 - Создать заметку \n2 - Удалить заметку \n3 - Изменить заметку \n4 - Найти заметку по Индексу \n5 - Найти заметку по дате написания \n6 - Показать все заметки \n7 - Выход\n\n Введите интересующий вас пункт меню: ")

