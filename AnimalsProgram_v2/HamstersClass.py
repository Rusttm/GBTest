from PetsMainClass import PetsMainClass


class HamstersClass(PetsMainClass):
    animal_type = "hamsters"
    animal_rus = "хомяк"
    def __init__(self): super().__init__()

if __name__ == '__main__':
    animal_type = HamstersClass()
    print(animal_type.get_animal_dict())