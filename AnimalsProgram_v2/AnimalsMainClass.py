from AnimalsLogger import AnimalsLogger


class AnimalsMainClass(AnimalsLogger):
    animal_group = None
    animal_type = None
    animal_name = None
    animal_commands = None

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    animal_class = AnimalsMainClass()
    print(animal_class)
