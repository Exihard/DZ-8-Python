# 8.2 ДОП ЗАДАЧА.
# Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. У нас труб будет больше.

# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна только одной данной 
# работающей трубой (в часах). Затем после пустой строки перечислены трубы, которые будут заполнять бассейн. Сколько минут
# на это потребуется?

# Номер трубы соответствует номеру строки, в которой записана ее производительность.

# Результат запишите в файл time.txt

# Пример
# Ввод

# 1
# 2
# 3
# (пустая строка)
# 1 2 3

# Вывод
# 32.72727272727273

f = open('pipes.txt', 'r')
f2 = open("time.txt", "w")
s = [line.rstrip() for line in f]
d = []
d1 = []
flag = 0
for i in s:
    if flag == 0:
        if i != '':
            d.append(eval(i))
        else:
            flag += 1
    else:
        s1 = i.split()
        for j in s1:
            d1.append(d[int(j) - 1])
f2.write(str(60 / sum([1 / i for i in d1]))) 
f2.close()
f.close()