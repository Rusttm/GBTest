from PetsMainClass import PetsMainClass


class DogsClass(PetsMainClass):
    animal_type = "dogs"
    def __init__(self): super().__init__()

if __name__ == '__main__':
    animal_type = DogsClass()
    print(animal_type.create_new_dict())
