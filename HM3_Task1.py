## Задание 1 (Урок 3)

## Создаем функцию нашего калькулятора для одного действия
def division():
    ## Для начала реализуем ввод пользователем чисел (делимого и делителя)
    arg_1 = int(input("Введите делимое число "))
    arg_2 = int(input("Введите делитель. Ноль не предлагать, мой код будет ругаться "))
    ## Проверяем, не ввел ли пользователь в графу делителя ноль. Уберегаем его от себя же....
    ## Если проверка пройдена, то функция выдаст результат деления, если же нет, то мы ругаем пользователя.
    if arg_2 !=0:
        result = arg_1 / arg_2
        print(result)
    else: 
        print("Деление на ноль ? Ну допустим ....")
        print("Нет. Его не будет,  и не проси")
        
division()