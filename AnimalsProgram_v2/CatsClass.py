from PetsMainClass import PetsMainClass


class CatsClass(PetsMainClass):
    animal_type = "cats"
    animal_rus = "кошка"

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    cat_obj = CatsClass()
    new_cat = cat_obj.add_new_animal("Kittie", "voice,eat")

    print(new_cat.get_animal_dict())
