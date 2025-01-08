first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y : x == y, first[0:min(len(first), len(second))], second[0:min(len(first), len(second))])))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for item in data_set:
                file.write(f"{item}\n")
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())