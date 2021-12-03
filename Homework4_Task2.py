
result_list = []
list_numbers = [int(i) for i in input("Введите числа: ").split()]

for i in range(1, len(list_numbers)):
    if list_numbers[i] > list_numbers[i-1]:
        (result_list.append(list_numbers[i]))

print("Исходные данные: ", list_numbers)
print("Элементы  больше предыдущих: ", result_list)