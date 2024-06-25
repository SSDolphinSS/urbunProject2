class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor < 1:
            print('"Такого этажа не существует"')
        a = 1
        for i in range(1, new_floor + 1):
            if new_floor > int(self.number_of_floor):
                print('"Такого этажа не существует"')
                break
            else:
                print(a)
                a += 1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(20)
h2.go_to(10)
