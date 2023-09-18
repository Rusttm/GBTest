from AnimalsProgram_v2.AnimalsLogger import AnimalsLogger


class AnimalsMainClass(AnimalsLogger):
    animal_group = None
    animal_type = None
    animal_name = None
    animal_commands = None

    def __init__(self):
        super().__init__()

    def create_new_dict(self) -> dict:
        return dict({"group": self.animal_group, "type": self.animal_type, "name": self.animal_name, "commands": self.animal_commands})


if __name__ == '__main__':
    animal_class = AnimalsMainClass()
    print(animal_class.create_new_dict())
