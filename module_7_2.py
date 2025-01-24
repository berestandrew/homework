def custom_write(file_name, strings):
    strings_positions = {}  # ключ - кортеж (<номер строки>, <байт начала строки>), # значение - записываемая строка
    line_number = 1
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            byte_position = file.tell()
            file.write(string + '\n')
            strings_positions[(line_number, byte_position)] = string
            line_number += 1

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')
