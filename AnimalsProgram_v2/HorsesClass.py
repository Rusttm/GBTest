from PacksMainClass import PacksMainClass


class HorsesClass(PacksMainClass):
    animal_type = "horses"
    def __init__(self): super().__init__()


if __name__ == '__main__':
    animal_type = HorsesClass()
    print(animal_type.create_new_dict())