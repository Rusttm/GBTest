# coding: utf8
class MenuMainClass:

    def print_main_menu(self):
        print()
        print("________________________________________")
        print("Нажмите:")
        print("1: для просмотра списка животных")
        print("2: для создания нового животного")
        print("3: для правки списка комманд животного")
        print("0: для выхода")


    def print_view_menu(self):
        print()
        print("________________________________________")
        print("Просмотр списка животных. 0 - завершить")


    def print_create_menu(self):
        print()
        print("________________________________________")
        print("Добавление нового животного.")

    def print_create1_menu(self):
        print("Введите тип животного:")
        print("1: Домашнее животное")
        print("2: Вьючное животное")
        print("0: для выхода")

    def print_create2_menu(self):
        print("Введите домашнее животное:")
        print("1: Кошка")
        print("2: Собака")
        print("3: Хомяк")
        print("0: для выхода")

    def print_create3_menu(self):
        print("Введите вьючное животное:")
        print("1: Лошадь")
        print("2: Верблюд")
        print("0: для выхода")

    def print_create_animal_name_menu(self):

        print("Введите кличку животного:")

    def print_create_animal_commands_menu(self):
        print("Введите через ',' комманды, которые животное знает:")

    def print_corr_menu(self, animals_list: list):
        print()
        print("________________________________________")
        print("Изменение комманд животного.\nКакое животное Вы хотите обучить?")
        i = 1
        for animal in animals_list:
            print(f"{i}: {animal}")
            i += 1
        print("0: для выхода")

    def print_corr1_menu(self, animal_name: str):
        print(f"Обучение животного.\nВведите новую комманду для {animal_name}: ")
        print("0: для выхода")
    def get_answer(self, right_answers_list: list = None) -> str:
        if right_answers_list:
            while True:
                user_answer = input(f"Нажмите один из предложенных вариантов {','.join(right_answers_list)}: ")
                if user_answer in right_answers_list:
                    return user_answer
        else:
            while True:
                user_answer = input(f"Введите любое значение, либо '0' для выхода: ")
                if user_answer:
                    return user_answer



if __name__ == '__main__':
    menu_creator = MenuMainClass()
    menu_creator.print_main_menu()

