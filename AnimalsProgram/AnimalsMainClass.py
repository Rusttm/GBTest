from AnimalsLogger import AnimalsLogger


class AnimalsMainClass(AnimalsLogger):
    kingdom_class = "animals"
    cur_db_list = None

    def __init__(self):
        super().__init__()
        self.load_db()

    def load_db(self):
        from ReadCsvClass import ReadCsv
        reader_csv = ReadCsv()
        try:
            self.cur_db_list = reader_csv.get_data()
        except Exception as e:
            self.logger.debug(f"{__class__.__name__} cant read data from db, error: {e}")
        else:
            self.logger.debug(f"{__class__.__name__} read data from db")


if __name__ == '__main__':
    connector = AnimalsMainClass()
    print(connector.cur_db_list)


