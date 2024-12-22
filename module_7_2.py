def custom_write(file_name: str, strings: list):
    strings_positions = {}
    number_line = 1
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        bytes_string = file.tell()
        file.write(f'{i}\n')
        strings_positions[(number_line, bytes_string)] = i
        number_line += 1
    file.close()
    return strings_positions

info = ['Text for tell.','Используйте кодировку utf-8.','Because there are 2 languages!','Спасибо!']

result = custom_write('Test.txt', info)
for elem in result.items():
    print(elem)

