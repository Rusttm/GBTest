from MenuMainClass import MenuMainClass


class ViewCreateClass(MenuMainClass):
    def __init__(self, animals_list: list):
        super().__init__()
        self.animals_list = animals_list

    def view_create_new_animal(self):
        while True:
            self.print_create_menu()
            self.print_create1_menu()
            user_answer = self.get_answer(["0", "1", "2", "3", "4", "5"])
            new_animal_obj = None
            if user_answer == "0":
                break
            elif user_answer == "1":
                # cat
                from CatsClass import CatsClass
                new_animal_obj = CatsClass()
            elif user_answer == "2":
                # dog
                from DogsClass import DogsClass
                new_animal_obj = DogsClass()
            elif user_answer == "3":
                # hamster
                from HamstersClass import HamstersClass
                new_animal_obj = HamstersClass()
            elif user_answer == "4":
                # horse
                from HorsesClass import HorsesClass
                new_animal_obj = HorsesClass()
            elif user_answer == "5":
                # camel
                from CamelsClass import CamelsClass
                new_animal_obj = CamelsClass()
            self.print_create_animal_name_menu()
            user_answer = input("? ")
            if (user_answer == "0") or (user_answer == ""):
                break
            else:
                new_animal_name = user_answer.capitalize()
            self.print_create_animal_commands_menu()
            user_answer = input("? ")
            if user_answer == "0":
                break
            else:
                new_animal_commands_str = user_answer.lower()
            for old_animal in self.animals_list:
                if (old_animal.animal_name == new_animal_name) and (old_animal.animal_type == new_animal_obj.animal_type):
                    res_string = f"{new_animal_obj.animal_rus.capitalize()} с такой кличкой уже существует, поэтому Не добавлено"
                    print(res_string)
                    return self.animals_list
            try:
                new_animal_obj.add_new_animal(new_animal_name, new_animal_commands_str)
                res_string = f"Животное {new_animal_obj.animal_name} успешно добавлено"
                print(res_string)
                self.animals_list.append(new_animal_obj)
            except Exception as e:
                print(e)
            else:
                from CountClass import CountClass
                counter = CountClass()
                counter.add()
            return self.animals_list





if __name__ == '__main__':
    new_view = ViewCreateClass()
    new_view.view_create_new_animal()
