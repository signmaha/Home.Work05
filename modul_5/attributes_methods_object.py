class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        floor = 0
        for floor in range(new_floor):
            print(floor + 1)
        if new_floor > self.number_of_floors or new_floor < self.number_of_floors:
            print(f'{new_floor + 1} такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, колличество этажей: {self.number_of_floors}"



#h1 = House('ЖК Горский', 18)
#h2 = House('Домик в деревне', 2)
#h1.go_to(5)
#h2.go_to(10)

h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

print(h1)

print(h2)

print(len(h1))

print(len(h2))
