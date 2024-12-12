data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    res = 0
    for i in data_structure:
        if isinstance(i, int):
            res += i
        elif isinstance(i, str):
            res += len(i)
        elif isinstance(i, list):
            res += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for k in i.keys():
                if isinstance(k, int):
                    res += k
                elif isinstance(k, str):
                    res += len(k)
                elif isinstance(k, tuple) or isinstance(k, set):
                    res += calculate_structure_sum(k)
            for v in i.values():
                if isinstance(v, int):
                    res += v
                elif isinstance(v, str):
                    res += len(v)
                elif isinstance(v, tuple) or isinstance(v, set) or isinstance(v, list) or isinstance(v, dict):
                    res += calculate_structure_sum(v)
        elif isinstance(i, tuple):
            res += calculate_structure_sum(i)
        elif isinstance(i, set):
            res += calculate_structure_sum(i)

    return res


result = calculate_structure_sum(data_structure)
print(result)
