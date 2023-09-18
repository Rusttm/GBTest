from AnimalsMainClass import AnimalsMainClass
from MenuMainClass import MenuMainClass


class MainClass(AnimalsMainClass, MenuMainClass):
    def __init__(self): super().__init__()


if __name__ == '__main__':
    connector = MainClass()