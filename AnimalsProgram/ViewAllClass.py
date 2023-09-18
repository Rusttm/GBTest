from MenuMainClass import MenuMainClass
from AnimalsMainClass import AnimalsMainClass


class ViewAllClass(AnimalsMainClass, MenuMainClass):
    def __init__(self): super().__init__()

    def view_all_db(self):
        while True:
            self.print_view_menu()
            for animal in self.cur_db_list:
                animal_genus = animal.get('genus', None)
                animal_genus_name = self.animals_genus_dict.get(animal_genus, None)
                animal_name = animal.get('name', None)
                print(f"{animal_genus_name.capitalize()} с кличкой {animal_name.capitalize()} знает комманды: {animal.get('commands', None)}")
            user_answer = self.get_answer(["0"])
            if user_answer == "0":
                break


if __name__ == '__main__':
    new_view = ViewAllClass()
    new_view.view_all_db()
