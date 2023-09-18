from AnimalsMainClass import AnimalsMainClass


class ReadCsv():
    """ class for getting info from csv file in main directory"""

    file_name = "animals_csv_db_utf.csv"

    def __init__(self):
        super().__init__()

    def get_data(self, file_name=None):
        if not file_name:
            file_name = self.file_name
        import csv
        with open(file_name, mode='r', encoding="utf-8-sig") as file:
            reader_csv = csv.reader(file)
            headers = next(reader_csv)
            result_list = [dict(zip(headers, i)) for i in reader_csv]
        return result_list

    def put_data(self, data_list=None, file_name=None):
        if not file_name:
            file_name = self.file_name
        import csv
        with open(file_name, mode='w', encoding="utf-8-sig") as file:
            for data_dict in data_list:
                headers = data_dict.keys()
                writer_csv = csv.DictWriter(file, headers)
                writer_csv.writeheader()
                writer_csv.writerow(data_dict)
        return True


if __name__ == '__main__':
    connector_csv = ReadCsv()
    data = connector_csv.get_data()
    print("data = ", data)
    # new_data = data.pop()
    # print(new_data)
    # connector_csv.put_data([new_data])
