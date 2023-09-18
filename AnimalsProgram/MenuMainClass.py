# coding: utf8
class MenuMainClass:

    def print_main_menu(self):
        print("Нажмите:")
        print("1: для просмотра списка животных")
        print("2: для создания нового животного")
        print("3: для правки списка комманд животного")
        print("0: для выхода")
        print()

    def print_view_menu(self):
        print("Просмотр списка животных. 0 - завершить")
        print()

    def print_create_menu(self):
        print("Создание нового животного. 0 - завершить")
        print()

    def print_corr_menu(self):
        print("Изменение комманд животного. 0 - завершить")
        print()

if __name__ == '__main__':
    menu_creator = MenuMainClass()
    menu_creator.print_main_menu()

