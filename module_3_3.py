def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=2, b=3)
print_params(b=3, c=False)
print_params(c=False, a=2)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [25, 'text', True]
values_dict = {'a': 33, 'b': 'email', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
