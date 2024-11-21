def print_params(a = 1, b = 'Строка', c = True):

    return (a, b, c)

print(print_params())
print(print_params(2))
print(print_params(2,'True'))
print(print_params(b = 25))
print(print_params(c = [1,2,3]))

values_list = [1, 'Строка', True]
values_dict = {"a": 1976, "b": 'Преподаватель', "c": True }

print(print_params(*values_list))
print(print_params(**values_dict))

values_list_2 = [54.32, 'Строка']
print(print_params(*values_list_2,42))
