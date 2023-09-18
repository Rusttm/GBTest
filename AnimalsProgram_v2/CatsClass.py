from PetsMainClass import PetsMainClass


class CatsClass(PetsMainClass):
    animal_type = "cats"
    def __init__(self): super().__init__()


if __name__ == '__main__':
    animal_type = CatsClass()
    print(animal_type.create_new_dict())
