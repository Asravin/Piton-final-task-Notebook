import Menu
import Functional as f

def play():
    input_command = " "
    while input_command != "6":
        Menu.list_program()
        input_command = input().strip()
        if input_command == "1" :
            f.note_add()



            
        if input_command == "4":
            f.searth_note("index")
        if input_command == "5":
            f.searth_note("date")
        break