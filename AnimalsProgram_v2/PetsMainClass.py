from AnimalsProgram_v2 import AnimalsMainClass


class PetsMainClass(AnimalsMainClass):
    animal_group = "pets"
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    pets_class = PetsMainClass()