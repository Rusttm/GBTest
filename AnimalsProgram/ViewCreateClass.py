from MenuMainClass import MenuMainClass
from AnimalsMainClass import AnimalsMainClass


class ViewCreateClass(AnimalsMainClass, MenuMainClass):
    def __init__(self): super().__init__()

    def view_create_new_animal(self):
        while True:
            self.print_create_menu()
            self.print_create1_menu()
            user_answer = self.get_answer(["0", "1", "2"])
            order_answer_dict = {"1": "pets", "2": "packs"}
            genus_pets_answer_dict = {"1": "cats", "2": "dogs", "3": "hamsters"}
            genus_packs_answer_dict = {"1": "horses", "2": "camels"}
            new_animal = dict({"kingdom": "animals"})
            if user_answer == "0":
                break
            elif user_answer == "1":
                animal_order = order_answer_dict.get(user_answer)
                self.print_create2_menu()
                user_answer = self.get_answer(["0", "1", "2", "3"])
                if user_answer == "0":
                    break
                else:
                    new_animal["order"] = genus_pets_answer_dict.get(user_answer)

            elif user_answer == "2":
                animal_order = order_answer_dict.get(user_answer)
                self.print_create3_menu()
                user_answer = self.get_answer(["0", "1", "2"])
                if user_answer == "0":
                    break
                else:
                    new_animal["genus"] = genus_packs_answer_dict.get(user_answer)

            self.print_create_animal_name_menu()
            user_answer = input("? ")
            if (user_answer == "0") or (user_answer == ""):
                break
            else:
                new_animal["name"] = user_answer.capitalize()
            self.print_create_animal_commands_menu()
            user_answer = input("? ")
            if user_answer == "0":
                break
            else:
                new_animal["commands"] = user_answer.lower()
            print(f"Добавляем новое животное: {new_animal=}")


if __name__ == '__main__':
    new_view = ViewCreateClass()
    new_view.view_create_new_animal()
