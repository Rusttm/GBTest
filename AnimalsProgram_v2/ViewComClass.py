import time

from MenuMainClass import MenuMainClass


class ViewComClass(MenuMainClass):

    def __init__(self, animals_list: list):
        super().__init__()
        self.animals_list = animals_list


    def view_change_animal_com(self):
        while True:


            if self.animals_list:
                names_list = []
                for animal in self.animals_list:
                    a_type = animal.animal_rus
                    a_name = animal.animal_name
                    a_commands_str = ', '.join(animal.animal_commands)
                    names_list.append(f"{a_type} {a_name} знает команды: {a_commands_str}")
            else:
                print("Список животных пуст")
                break
            self.print_corr_menu(names_list)
            # list of names: commands
            user_answer = self.get_answer([str(pos) for pos in range(len(self.animals_list)+1)])
            if (user_answer == "0") or (user_answer == ""):
                break
            else:
                animal_index = int(user_answer)-1
                animal = self.animals_list[animal_index]
                # print(animal.animal_name)
                # animal_commands = animal.get("commands", None)
                animal_name = animal.animal_name
                # if animal_commands:
                #     commands_list = str(animal_commands).split(',')
                self.print_corr1_menu(animal_name)
                user_answer = self.get_answer()

            if (user_answer == "0") or (user_answer == ""):
                print(f"{animal_name} дополнительно не обучился.")
                return self.animals_list
            elif user_answer in animal.animal_commands:
                print(f"{animal_name} уже знает эту комманду.")
                return self.animals_list
            else:
                new_command = user_answer
                animal.add_command(new_command)
                print(f"{animal_name} обучился комманде '{new_command}'")
                time.sleep(2)
                return self.animals_list


if __name__ == '__main__':
    new_view = ViewComClass()
    new_view.view_change_animal_com()
