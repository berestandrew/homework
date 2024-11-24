my_dict = {'Ivan': 27, 'Oleg': 33, 'Pavel': 40}
print(my_dict)
print(my_dict.get('Pavel'))
print(my_dict.get('Liza'))
my_dict.update({'Anna': 36, 'Masha': 22})
print(my_dict.pop('Oleg'))
print(my_dict)

my_set = {5, 10, 20, 15, 5, 10}
print(my_set)
my_set.update({25, 30})
my_set.remove(30)
print(my_set)
