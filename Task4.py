## Вводим свободный набор чисел, отсортированных в порядке убывания
my_list = [5, 4, 3, 2, 1]


## Тут небольшой костыль, нужный для того, чтобы запустить цикл while дальше по коду
print(f"Рейтинг - {my_list}")
user_input_1 = int(input("Введите число "))

## Функция для подсчета рейтинга. Ее можно описать таким образом : проверка сценария инпута либо больше чего-то , либо равно, либо ставится в конец. Потом этот алгоритм нужно зациклить

def rating():
    length = len(my_list)
    user_input = int(input("Введите число "))
    for i in range(length-1):
        if user_input > my_list[i]:
            my_list.insert(i, user_input)
            break
        elif user_input == my_list[i]:
            my_list.insert(i+1, user_input)
            break
        elif user_input < my_list[length-1]:
            my_list.append(user_input)
            break
while user_input_1 != 000:
    
    rating()    
  
    print(my_list)      
