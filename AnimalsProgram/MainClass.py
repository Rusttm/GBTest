from AnimalsMainClass import AnimalsMainClass
from MenuMainClass import MenuMainClass


class MainClass(MenuMainClass):
    def __init__(self):
        super().__init__()
        self.AnimalsMainClass = AnimalsMainClass

    def start_program(self):
        btn_command = "start"
        while btn_command != "0":
            self.print_main_menu()
            user_answer = self.get_answer(["0", "1", "2"])
            if user_answer == "1":
                from ViewAllClass import ViewAllClass
                ViewAllClass(self.AnimalsMainClass()).view_all_db()
            elif user_answer == "2":
                from ViewCreateClass import ViewCreateClass
                ViewCreateClass(self.AnimalsMainClass()).view_create_new_animal()
        return True


if __name__ == '__main__':
    connector = MainClass()
    connector.start_program()
