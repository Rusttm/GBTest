from PetsMainClass import PetsMainClass


class HamstersClass(PetsMainClass):
    animal_type = "hamsters"
    def __init__(self): super().__init__()

if __name__ == '__main__':
    animal_type = HamstersClass()
    print(animal_type.create_new_dict())