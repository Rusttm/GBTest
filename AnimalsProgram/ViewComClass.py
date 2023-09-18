from MenuMainClass import MenuMainClass


class ViewComClass(MenuMainClass):
    def __init__(self, AnimalsMainClass): 
        super().__init__()
        self.AnimalsMainClass = AnimalsMainClass

    def view_change_animal_com(self):
        while True:
            animals_list = self.AnimalsMainClass.cur_db_list
            if animals_list:
                names_list = [animal.get("name", None) + ": " + animal.get("commands", None) for animal in animals_list]
            else:
                names_list = None
            self.print_corr_menu(names_list)
            # list of names: commands
            user_answer = self.get_answer([str(pos) for pos in range(len(animals_list)+1)])
            if (user_answer == "0") or (user_answer == ""):
                break
            else:
                animal_index = int(user_answer)-1
                animal = animals_list[animal_index]
                animal_commands = animal.get("commands", None)
                animal_name = animal.get("name", None)
                if animal_commands:
                    commands_list = str(animal_commands).split(',')
                self.print_corr1_menu(animal_name)
                user_answer = self.get_answer()

            if (user_answer == "0") or (user_answer == ""):
                print(f"{animal_name} дополнительно не обучился.")
                break
            else:
                new_command = user_answer
                animal["commands"] = animal.get("commands", None) + "," + new_command
                self.AnimalsMainClass.cur_db_list.pop(animal_index)
                self.AnimalsMainClass.cur_db_list.append(animal)
                self.AnimalsMainClass.save_db()





if __name__ == '__main__':
    new_view = ViewComClass()
    new_view.view_change_animal_com()
