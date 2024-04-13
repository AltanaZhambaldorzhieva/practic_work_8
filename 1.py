n = int(input('Введите результат'))
k = 0

while n != -1:
    n = int(input('Введите результат'))
    if k < n:
        k = n
    else:
        k = 0

print(k)


