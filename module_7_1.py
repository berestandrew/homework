class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

        with open(self.__file_name, 'a', encoding='utf-8'):
            pass

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            return file.read()

    def add(self, *products):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            current_products = file.read().splitlines()

        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if str(product) not in current_products:
                    file.write(str(product) + '\n')
                else:
                    print(f"Продукт {product.name} уже есть в магазине")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# Вывод на консоль:
# Первый запуск:
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
