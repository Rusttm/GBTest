from PetsMainClass import PetsMainClass


class DogsClass(PetsMainClass):
    animal_type = "dogs"
    animal_rus = "собака"
    def __init__(self): super().__init__()

if __name__ == '__main__':
    animal_type = DogsClass()
    print(animal_type.get_animal_dict())
