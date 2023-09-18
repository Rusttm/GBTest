from AnimalsMainClass import AnimalsMainClass
from MenuMainClass import MenuMainClass


class MainClass(AnimalsMainClass, MenuMainClass):
    def __init__(self): super().__init__()

    def start_program(self):
        btn_command = "start"
        while btn_command != "0":
            self.print_main_menu()
            user_answer = self.get_answer(["0", "1", "2"])
            if user_answer == "1":
                from ViewAllClass import ViewAllClass
                ViewAllClass().view_all_db()
            elif user_answer == "2":
                from ViewCreateClass import ViewCreateClass
                ViewCreateClass().print_create_menu()
        return True


if __name__ == '__main__':
    connector = MainClass()
    connector.start_program()
