import time

from MenuMainClass import MenuMainClass


class ViewAllClass(MenuMainClass):
    animals_list = None
    keys_converter = {'group': 'группа', 'type': 'тип животного', 'name': 'имя', 'commands': 'команды'}
    values_converter = {'pets': 'домашние животные', 'packs': 'вьючные животные'}

    def __init__(self, animals_list: list):
        super().__init__()
        self.animals_list = animals_list

    def view_all_animals(self):
        if not self.animals_list:
            print("Список животных пуст")
        else:
            while True:
                self.print_view_menu()
                i = 1
                for animal in self.animals_list:
                    print(f"{i}: {animal.animal_rus.capitalize()} {animal.animal_name.capitalize()} ")
                    i += 1
                user_answer = self.get_answer([str(s) for s in range(i)])
                if user_answer == "0":
                    break
                else:
                    animal = self.animals_list[int(user_answer)-1]
                    a_type = animal.animal_rus.capitalize()
                    a_name = animal.animal_name.capitalize()
                    a_commands = ', '.join(animal.animal_commands)
                    if a_commands:
                        print(f"{a_type} {a_name} знает команды {a_commands}")
                    else:
                        print(f"{a_type} {a_name} ничего не умеет")
                    time.sleep(2)


if __name__ == '__main__':
    new_view = ViewAllClass()
    new_view.view_all_animals()
