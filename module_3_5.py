def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        first=int(str_number)
        if first == 0:
            first = 1
        return first

result = get_multiplied_digits(40203000)
print(result)

