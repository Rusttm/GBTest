from AnimalsMainClass import AnimalsMainClass


class ConnCsv():
    """ class for getting info from csv file in main directory"""

    file_name = "animals_csv_db_utf.csv"

    def __init__(self):
        super().__init__()

    def get_data(self, file_name=None):
        if not file_name:
            file_name = self.file_name
        import csv
        try:
            with open(file_name, mode='r', encoding="utf-8-sig") as file:
                reader_csv = csv.reader(file)
                headers = next(reader_csv)
                result_list = [dict(zip(headers, i)) for i in reader_csv]
            return result_list
        except StopIteration:
            print(f"Database doesnt contain data")
            return None

    def put_data(self, data_list=None, file_name=None):
        if not file_name:
            file_name = self.file_name
        import csv
        with open(file_name, mode='w', encoding="utf-8-sig") as file:
            headers = data_list[0].keys()
            writer_csv = csv.DictWriter(file, headers)
            writer_csv.writeheader()
            for data_dict in data_list:
                writer_csv.writerow(data_dict)
        return True


if __name__ == '__main__':
    connector_csv = ConnCsv()
    data = connector_csv.get_data()
    print("data = ", data)
    data_list = [
        {'kingdom': 'animals', 'order': 'pets', 'genus': 'dogs', 'name': 'Alfie', 'commands': 'come, sit, lay, stand'},
        {'kingdom': 'animals', 'order': 'packs', 'genus': 'horses', 'name': 'Roach', 'commands': 'come, go, stop'},
        {'kingdom': 'animals', 'order': 'pets', 'genus': 'cats', 'name': 'Kittie', 'commands': 'come, sit, lay'},
        {'kingdom': 'animals', 'order': 'pets', 'genus': 'dogs', 'name': 'Peppa', 'commands': 'come, sit, lay, stand'},
        {'kingdom': 'animals', 'order': 'pets', 'genus': 'cats', 'name': 'Ralf', 'commands': 'come, sit, lay, stand'}]

    connector_csv.put_data(data_list)
