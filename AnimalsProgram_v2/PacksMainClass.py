from AnimalsMainClass import AnimalsMainClass


class PacksMainClass(AnimalsMainClass):
    animal_group = "packs"
    animal_group_rus = "вьючное животное"
    def __init__(self): super().__init__()


if __name__ == '__main__':
    animal_group = PacksMainClass()
    print(animal_group.get_animal_dict())
