def get_multiplied_digits(numbers):
    str_number = (str(numbers)).replace('0', '')
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)

# Выводнаконсоль:
# 24
# 24