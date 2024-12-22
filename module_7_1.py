class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name  # Название
        self.weight = weight  #  Вес
        self.category = category  # Категория

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name,'r')
        file_contents = file.read()
        file.close()
        return file_contents

    def add(self, *products: Product):
        list_products = []
        file = open(self.__file_name, 'a+')  # a+ считывает и добавляет информацию в файл
        file.seek(0)    # переходим в начало файла
        for i in file:
            list_products.append(i.rstrip()) # rstrip() - удаляет  последний символ в строке (конец строки. \n)
        for j in products:
            if str(j) in list_products:
                print(f'Продукт {j} уже есть в магазине')
            else:
                file.write(f'{j}\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())