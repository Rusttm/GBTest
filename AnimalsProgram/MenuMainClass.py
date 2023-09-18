# coding: utf8
class MenuMainClass:

    def print_main_menu(self):
        print("Нажмите:")
        print("1: для просмотра списка животных")
        print("2: для создания нового животного")
        print("3: для правки списка комманд животного")
        print("0: для выхода")


    def print_view_menu(self):
        print("Просмотр списка животных. 0 - завершить")


    def print_create_menu(self):
        print("Создание нового животного.")

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

    def print_corr_menu(self):
        print("Изменение комманд животного. 0 - завершить")

    def get_answer(self, right_answers_list: list) -> str:
        while True:
            user_answer = input(f"Нажмите одни из предложенных вариантов {','.join(right_answers_list)}:")
            if user_answer in right_answers_list:
                return user_answer




if __name__ == '__main__':
    menu_creator = MenuMainClass()
    menu_creator.print_main_menu()

