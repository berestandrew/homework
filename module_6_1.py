class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):

    def eat(self, food):
        self.food = self.name
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False


class Predator(Animal):

    def eat(self, food):
        self.food = self.name
        if Plant.edible == True:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False


class Flower(Plant):
    edible = False


class Fruit(Plant):
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

# Вывод на консоль:
# Волк с Уолл-Стрит
# Цветик семицветик
# True
# False
# Волк с Уолл-Стрит не стал есть Цветик семицветик
# Хатико съел Заводной апельсин
# False
# True
