
from MenuMainClass import MenuMainClass

class MainClass(MenuMainClass):
    animals_list = list()
    def __init__(self):
        super().__init__()

    def start_program(self):
        user_answer = "start"
        while user_answer != "0":
            self.print_main_menu()
            user_answer = self.get_answer(["0", "1", "2", "3"])
            if user_answer == "1":
                from ViewAllClass import ViewAllClass
                ViewAllClass(self.animals_list).view_all_animals()
            elif user_answer == "2":
                from ViewCreateClass import ViewCreateClass
                create_view = ViewCreateClass(self.animals_list)
                self.animals_list = create_view.view_create_new_animal()
            elif user_answer == "3":
                from ViewComClass import ViewComClass
                commands_view = ViewComClass(self.animals_list)
                commands_view.view_change_animal_com()
        return True


if __name__ == '__main__':
    connector = MainClass()
    from CatsClass import CatsClass
    cat_obj = CatsClass()
    new_cat = cat_obj.add_new_animal("Kittie", "voice,eat")
    connector.animals_list.append(new_cat)
    from HorsesClass import HorsesClass
    new_horse = HorsesClass().add_new_animal("Roach", "go")
    connector.animals_list.append(new_horse)

    connector.start_program()
