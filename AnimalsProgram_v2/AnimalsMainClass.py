from AnimalsProgram_v2.AnimalsLogger import AnimalsLogger


class AnimalsMainClass(AnimalsLogger):
    animal_group = None
    animal_type = None
    animal_name = None
    animal_commands = list()

    def __init__(self):
        super().__init__()

    def add_name(self, name:str):
        self.animal_name = name.capitalize()

    def add_command(self, command: str):
        self.animal_commands.append(command.lower())

    def get_commands_str(self) -> str:
        return ', '.join(self.animal_commands)

    def create_new_dict(self) -> dict:
        return dict({"group": self.animal_group, "type": self.animal_type, "name": self.animal_name, "commands": self.animal_commands})


if __name__ == '__main__':
    animal_class = AnimalsMainClass()
    print(animal_class.create_new_dict())
