from AnimalsLogger import AnimalsLogger


class AnimalsMainClass(AnimalsLogger):
    kingdom_class = "animals"
    cur_db_list = None
    db_headers = ["kingdom", "order", "genus", "name", "commands"]
    animals_genus_dict = {"horses": "лошадь", "cats": "кошка", "dogs": "собака", "hamsters": "хомяк", "camels": "верблюд"}

    def __init__(self):
        super().__init__()
        self.load_db()

    def load_db(self):
        from ConnCsvClass import ConnCsv
        reader_csv = ConnCsv()
        try:
            self.cur_db_list = reader_csv.get_data()
        except Exception as e:
            self.logger.debug(f"{__class__.__name__} cant read data from db, error: {e}")
            return False
        else:
            self.logger.debug(f"{__class__.__name__} read data from db")
            return True

    def save_db(self):
        from ConnCsvClass import ConnCsv
        writer_csv = ConnCsv()
        try:
            writer_csv.put_data(data_list=self.cur_db_list)
        except Exception as e:
            self.logger.debug(f"{__class__.__name__} cant write data to db, error: {e}")
            return False
        else:
            self.logger.debug(f"{__class__.__name__} wrote data to db")
            return True

    def add_new_animal_db(self, animal_dict: dict):
        """ checks new dict and add new animal"""
        for old_dict in self.cur_db_list:
            # checks for name duplicate
            animal_name = old_dict.get("name", None)
            new_animal_name = animal_dict.get("name", None)
            if animal_name == new_animal_name:
                self.logger.debug(f"{__class__.__name__} animal with name {animal_name} already exist {old_dict}")
                return False

        for head in self.db_headers:
            # checks for correct headers
            if not animal_dict.get(head, None):
                self.logger.debug(f"{__class__.__name__} wrong field name for {head}")
                return False
        self.cur_db_list.append(animal_dict)
        if not self.save_db():
            # tries to write
            self.cur_db_list.pop()
            return False
        return True


if __name__ == '__main__':
    connector = AnimalsMainClass()
    print(connector.cur_db_list)
    print(connector.add_new_animal_db({'order': 'pets', 'genus': 'dogs', 'name': 'Peppa', 'commands': 'come, sit, lay, stand'}))
    data_list = [{'kingdom': 'animals', 'order': 'pets', 'genus': 'dogs', 'name': 'Alfie', 'commands': 'come, sit, lay, stand'},
     {'kingdom': 'animals', 'order': 'packs', 'genus': 'horses', 'name': 'Roach', 'commands': 'come, go, stop'},
     {'kingdom': 'animals', 'order': 'pets', 'genus': 'cats', 'name': 'Kittie', 'commands': 'come, sit, lay'},
     {'kingdom': 'animals', 'order': 'pets', 'genus': 'dogs', 'name': 'Peppa', 'commands': 'come, sit, lay, stand'},
     {'kingdom': 'animals', 'order': 'pets', 'genus': 'cats', 'name': 'Ralf', 'commands': 'come, sit, lay, stand'}]

    print(connector.add_new_animal_db(
        {'kingdom': 'animals', 'order': 'pets', 'genus': 'cats', 'name': 'Ralf', 'commands': 'come, sit, lay, stand'}))
