## Создаем функцию, которая делает слово с первой заглавной буквы
def int_func(text):
    return text.title()


output = []
## Реализуем функционал сбора слов с пользователя
for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    output.append(int_func(word))

print(f'Вариант1 Строка получается вот такая: {" ".join(output)}')
