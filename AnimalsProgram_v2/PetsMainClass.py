from AnimalsProgram_v2.AnimalsMainClass import AnimalsMainClass


class PetsMainClass(AnimalsMainClass):
    animal_group = "pets"

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    animal_group = PetsMainClass()
    print(animal_group.create_new_dict())
