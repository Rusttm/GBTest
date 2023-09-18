from AnimalsMainClass import AnimalsMainClass


class ReadCsv(AnimalsMainClass):
    """ class for getting info from csv file in main directory"""

    file_name = "animals_csv_db_utf.csv"
    def __init__(self): super().__init__()

    def get_data(self, file_name=None):
        if not file_name:
            file_name = self.file_name
        import csv
        with open(file_name, mode='r', encoding="utf-8-sig") as file:
            reader_csv = csv.reader(file)
            headers = next(reader_csv)
            result_list = [dict(zip(headers, i)) for i in reader_csv]
        return result_list


if __name__ == '__main__':
    reader = ReadCsv()
    print(reader.get_data())


