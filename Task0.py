
## Задание 1.Работа с типами данных
## Сделаем список с кучей разномастных  данных
my_list = ["word", 1.0, 18.0, 1984, ["list","list_2"]]
## Создаем функцию, которая будет определять по элементу списка его тип
def type_checking(list_element):
    current_type = type(list_element)
    print(current_type)
## Проверяем работу функции
type_checking(my_list[4])    
## Создаем цикл перебирающий вксь список элементов и проверяющий их типы
for i in range(5):
    type_checking(my_list[i])