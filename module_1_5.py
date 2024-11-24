immutable_var = (236, 'home', False)
print(immutable_var)
# immutable_var[0] = 'one' - TypeError: 'tuple' object does not support item assignment
# кортеж - неизменяемый тип данных

mutable_list = [34, 256, 'ONE', 'text']
mutable_list[1] = 'num'
print(mutable_list)
