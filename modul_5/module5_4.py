class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        if args:
            cls.houses_history.append(args[0])
            return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f" {self.name}, снесён ,но он останется в истории")

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

    def __eq__(self, value):
        if isinstance(value, House):
            return self.number_of_floors == value.number_of_floors

    def __it__(self, value):
        if isinstance(value, House):
            return self.number_of_floors < value.number_of_floors

    def __le__(self, value):
        if isinstance(value, House):
            return self.number_of_floors <= value.number_of_floors

    def __gt__(self, value):
        if isinstance(value, House):
            return self.number_of_floors > value.number_of_floors

    def __ge__(self, value):
        if isinstance(value, House):
            return self.number_of_floors >= value.number_of_floors

    def __ne__(self, value):
        if isinstance(value, House):
            return self.number_of_floors != value.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self


# Пример использования класса
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # Вывод: ЖК Акация снесён, но он останется в истории
del h3  # Вывод: ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
