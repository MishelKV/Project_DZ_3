def calculate_structure_sum(*args):
    sum_element = 0

    for i in args:
        if isinstance(i, str):
            sum_element += len(i)
        elif isinstance(i, int):
            sum_element += i
        elif isinstance(i, float):
            sum_element += i
        elif isinstance(i, bool):
            sum_element += i
        elif isinstance(i, list):
            sum_element += calculate_structure_sum(*i)
        elif isinstance(i, tuple):
            sum_element += calculate_structure_sum(*i)
        elif isinstance(i, set):
            sum_element += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            sum_element += calculate_structure_sum(*tuple(i.items()))
    return sum_element

data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),
                  "Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
