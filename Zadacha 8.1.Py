# Задача 8.1 Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно
# последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). 
# Протестируем функцию на файле «article.txt» со следующим содержимым:

def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
    else:
        print('Количество строк может быть только целым положительным')

print('Тест №1')
n = int(input('Введите положительное число строк для вывода: '))
read_last(n, 'article.txt')
print('Тест №2')
m = int(input('Введите отрицательное число строк для вывода: '))
read_last(m, 'article.txt')