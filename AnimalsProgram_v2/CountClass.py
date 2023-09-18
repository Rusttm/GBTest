class CountClass:
    __count: int = 0

    def add(self):
        self.__count += 1

    def get(self):
        return self.__count

if __name__ == '__main__':
    new_count_obj = CountClass()
    print(new_count_obj.add())
    print(new_count_obj.add())
    print(new_count_obj.get())