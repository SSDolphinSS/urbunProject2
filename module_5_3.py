class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    # def go_to(self, new_floor):
    #     if new_floor < 1 or new_floor > self.number_of_floor:
    #         print('Такого этажа не существует')
    #     else:
    #         for i in range(1, new_floor + 1):
    #             print(i)
    #             i += 1

    # def __len__(self):
    #     return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floor}'

    def __del__(self):
        print(f'{self.name} cнесен, но он останется в истории')

    # def __eq__(self, other):
    #     return self.number_of_floor == other.number_of_floor
    #
    # def __add__(self, other):
    #     self.number_of_floor += other
    #     return self
    #
    # def __iadd__(self, other):
    #     return self.__add__(other)
    #
    # def __radd__(self, other):
    #     return self.__add__(other)
    #
    # def __gt__(self, other):
    #     return self.number_of_floor > other.number_of_floor
    #
    # def __ge__(self, other):
    #     return self.number_of_floor >= other.number_of_floor
    #
    # def __lt__(self, other):
    #     return self.number_of_floor < other.number_of_floor
    #
    # def __le__(self, other):
    #     return self.number_of_floor <= other.number_of_floor
    #
    # def __ne__(self, other):
    #     return self.number_of_floor != other.number_of_floor


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрешки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# h1.go_to(5)
# h2.go_to(10)
#
# # __str__
# print(h1)
# print(h2)
#
# # __len__
# print(len(h1))
# print(len(h2))

# print(h1 == h2)  # __eq__
#
# h1 = h1 + 10  # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10  # __iadd__
# print(h1)
#
# h2 = 10 + h2  # __radd__
# print(h2)
#
# print(h1 > h2)  # __gt__
# print(h1 >= h2)  # __ge__
# print(h1 < h2)  # __lt__
# print(h1 <= h2)  # __le__
# print(h1 != h2)  # __ne__
