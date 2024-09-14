def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function() #нет в консоли

test_function() # работает
inner_function() #ошибка, inner_function является локальной функцией внутри test_function и не доступна за пределами этой функции.

