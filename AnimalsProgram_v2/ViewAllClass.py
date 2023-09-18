from MenuMainClass import MenuMainClass


class ViewAllClass(MenuMainClass):
    animals_list = None
    keys_converter = {'group': 'группа', 'type': 'тип животного', 'name': 'имя', 'commands': 'комманды'}
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
                for animal in self.animals_list:
                    animal_dict = animal.get_animal_dict()
                user_answer = self.get_answer(["0"])
                if user_answer == "0":
                    break


if __name__ == '__main__':
    new_view = ViewAllClass()
    new_view.view_all_animals()
