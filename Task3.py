
sentence = input("Введите предложение ")

word = []
number = 1

for element in range(sentence.count(' ') + 1):
    word  = sentence.split()
    if len(str(word)) <= 10:
        print(f" {number} {word  [element]}")
        number += 1
    else:
        print(f" {number} {word  [element] [0:10]}")
        number += 1