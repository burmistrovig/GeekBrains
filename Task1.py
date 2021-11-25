
## Реализуем ввод пользователем количества вводимых данных (для удобства)
element_count = int(input("Введите количество элементов списка "))
## Объявляем пустые переменные, которые мы впоследствии будем юзать

my_list = []
i = 0
element = 0

## Реализуем ввод данных пользователем. Ориентирумся на предыдущий инпут

while i < element_count:
    my_list.append(input("Введите значение списка "))
    i += 1
## А вот уже и занимаемся переменой мест слагаемых

for elem in range(int(len(my_list)/2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2

## Вывод измененного списка 
print(my_list)