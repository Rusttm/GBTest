from AnimalsProgram import AnimalsMainClass


class PetsMainClass(AnimalsMainClass):
    order_class = "pets"
    def __init__(self): super().__init__()
