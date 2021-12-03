from functools import reduce

list_numbers = [i for i in range(100, 1001, 2)]

print("Четные числа в диапазоне [100..1000]:\n", list_numbers)
print("Произведение :\n", reduce(lambda x,y: x*y, list_numbers))