# Позиционирование в файле. Закрепить знания о позиционировании в файле, использовав метод tell()
# файлового объекта. Написать усовершенствованную функцию записи.

from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}  # Создаем пустой словарь
    num_str = 0  # номер строки
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        num_str += 1
        pos = file.tell()  # находим позицию курсора
        file.write(f'{i}\n')
        strings_positions[num_str, pos] = i  # наполняем словарь ключом явл-ся кортеж
        # (<номер строки>, <байт начала строки>), а значением - записываемая строка
    file.close()
    file = open(file_name, 'r', encoding='utf-8')
    pprint(file.read())
    file.close()
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
