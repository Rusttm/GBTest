from AnimalsMainClass import AnimalsMainClass
from MenuMainClass import MenuMainClass


class MainClass(AnimalsMainClass, MenuMainClass):
    def __init__(self): super().__init__()

    def start_program(self):
        btn_command = "start"
        while btn_command != "0":
            self.print_main_menu()
            btn_command = input("? ")
            if btn_command == "1":
                from ViewAllClass import ViewAllClass
                ViewAllClass().view_all_db()
        return True


if __name__ == '__main__':
    connector = MainClass()
    connector.start_program()
