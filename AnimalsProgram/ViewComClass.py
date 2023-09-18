from MenuMainClass import MenuMainClass


class ViewComClass(MenuMainClass):
    def __init__(self, AnimalsMainClass): 
        super().__init__()
        self.AnimalsMainClass = AnimalsMainClass

    def view_change_animal_com(self):
        while True:
            animals_list = self.AnimalsMainClass.cur_db_list
            if animals_list:
                names_list = [animal.get("name", None) for animal in animals_list]
            else:
                names_list = None
            self.print_corr_menu(names_list)
            user_answer = self.get_answer([str(pos) for pos in range(len(animals_list)+1)])
            if (user_answer == "0") or (user_answer == ""):
                break




if __name__ == '__main__':
    new_view = ViewComClass()
    new_view.view_create_new_animal()
