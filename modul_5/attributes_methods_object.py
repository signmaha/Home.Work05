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


h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h2.go_to(10)
