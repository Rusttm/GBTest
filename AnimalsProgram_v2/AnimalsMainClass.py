from AnimalsLogger import AnimalsLogger


class AnimalsMainClass(AnimalsLogger):
    animal_group = None
    animal_type = None
    animal_name = None
    animal_commands = list()

    def __init__(self):
        super().__init__()

    def add_new_animal(self, name: str, commands_str: str):
        self.add_name(name)
        self.animal_commands = commands_str.split(', ')
        return self

    def add_name(self, name: str):
        self.animal_name = name.capitalize()

    def add_command(self, command_str: str):
        commands_str_list = command_str.lower().split(',')
        self.animal_commands += commands_str_list

    def get_commands_str(self) -> str:
        return ', '.join(self.animal_commands)

    def get_animal_dict(self) -> dict:
        return dict({"group": self.animal_group, "type": self.animal_type, "name": self.animal_name, "commands": self.animal_commands})


if __name__ == '__main__':
    animal_class = AnimalsMainClass()
    print(animal_class.get_animal_dict())
