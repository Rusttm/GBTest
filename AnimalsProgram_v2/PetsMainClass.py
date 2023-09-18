from AnimalsMainClass import AnimalsMainClass


class PetsMainClass(AnimalsMainClass):
    animal_group = "pets"
    animal_group_rus = "домашнее животное"

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    animal_group = PetsMainClass()
    print(animal_group.get_animal_dict())
