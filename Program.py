import Menu
import functional as f

def play():
    input_command = ''
    while input_command != '7':
        Menu.list_program()
        input_command = input().strip()
        if input_command == '1':
            f.note_add()
        if input_command == '2':
            f.searth_note('all')
            f.delete_and_edit('delete')
        if input_command == '3':
            f.searth_note('all')
            f.delete_and_edit('edit')
        if input_command == '4':
            f.searth_note('id')
            f.delete_and_edit('searth_note')
        if input_command == '5':
            f.searth_note('date')
        if input_command == '6':
            f.searth_note('all')
        if input_command == '7':
            print("Завершение работы программы")
            break