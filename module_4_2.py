def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()  # Ничего не возвращает.


inner_function()  # Ошибка, мы не можем вызвать функцию в другом пространстве имен.


test_function()
