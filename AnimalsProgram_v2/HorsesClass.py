from PacksMainClass import PacksMainClass


class HorsesClass(PacksMainClass):
    animal_type = "horses"
    animal_rus = "лошадь"
    def __init__(self): super().__init__()


if __name__ == '__main__':
    animal_type = HorsesClass()
    print(animal_type.get_animal_dict())