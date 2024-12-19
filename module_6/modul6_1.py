class Animal:
    alive = True
    fed = False


def __init__(self, name):
    self.name = name


class Predator(Animal):

    def eat(self, *food):
        if isinstance(food, Plant):

            if food.edible:
                print(f'{self.name},съел {self.food}')
                fed = True
            else:
                print(f'{self.name},не стал есть {self.food}')
                alive = False


class Mammal(Animal):


    class Plant:
     edible = False

    def __init__(self, name):
      self.name = name


   class Flower(Plant):

    class Fruit(Plant):
        def __init__(self, name):
            super(self.name)
            edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
