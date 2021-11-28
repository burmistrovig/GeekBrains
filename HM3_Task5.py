## Задание 5 (Урок 3)




## Создаем функцию, которая проверяет, ввели мы число ( и тогда суммирует все) или любую букву-ключ, и тогда все прекращается
def calculations(*nums):
    sums = 0
    for element in numbers:
        if element != "A":
            element = int(element)
            sums+= element
        else:
            print("ERROR! WARNING! AN END ONCE AND FOR ALL")
            break
    return sums
    

general_sum = 0
## Создаем цикл, в котором будет запрашиваться ввод данных пользователем до стоп-ключа
while True : 
    numbers = input("Введите числа через пробел ").split(' ')
    general_sum += calculations(numbers)
    print(general_sum) 
    
calculations(numbers)

