from PacksMainClass import PacksMainClass


class CamelsClass(PacksMainClass):
    animal_type = "camels"
    animal_rus = "верблюд"
    def __init__(self): super().__init__()


if __name__ == '__main__':
    animal_type = CamelsClass()
    print(animal_type.get_animal_dict())
