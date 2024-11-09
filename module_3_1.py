calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls() # Вызов функции string
    length_string = len(string) # Подсчет количества букв в слове
    upper_string = string.upper() # Строка в верхнем регистре
    lower_string = string.lower() # Строка в нижнем регистре
    return (length_string, upper_string, lower_string)

def is_contains(string, list_to_search):
    count_calls() # Вызов функции string
    s_lower = string.lower() # Ввод аргумента строка
    list_to_search_lower = [item.lower() for item in list_to_search]
    return s_lower in list_to_search_lower

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # True
print(is_contains('cycle', ['recycling', 'cyclic'])) # False
print(calls)

