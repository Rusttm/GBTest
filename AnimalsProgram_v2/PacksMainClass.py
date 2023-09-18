from AnimalsProgram_v2.AnimalsMainClass import AnimalsMainClass


class PacksMainClass(AnimalsMainClass):
    animal_group = "packs"
    def __init__(self): super().__init__()


if __name__ == '__main__':
    animal_group = PacksMainClass()
    print(animal_group.create_new_dict())
