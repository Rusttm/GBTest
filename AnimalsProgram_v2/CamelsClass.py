from PacksMainClass import PacksMainClass


class CamelsClass(PacksMainClass):
    animal_type = "camels"
    def __init__(self): super().__init__()


if __name__ == '__main__':
    animal_type = CamelsClass()
    print(animal_type.create_new_dict())
