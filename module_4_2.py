def  test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() # эта функция не срабатывает без вызова функции test_function(),
    # потому что она находится внутри ее пространства. Вызвав функцию test_function(),
    # в глобальном пространстве она начинает работать



#inner_function() # функция inner_function была создана внутри пространства функции test_function,
# поэтому она не вызывается за ее пределами


test_function()








