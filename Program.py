import Menu
import Functional as f

def play():
    input_command = " "
    while input_command != "3":
        Menu.list_program()
        input_command = input().strip()
        if input_command == "1" :
            f.note_add()
        break