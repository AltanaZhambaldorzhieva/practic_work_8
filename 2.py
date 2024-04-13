n = int(input('Введите результат'))
k = 0
count = 0

while n != -1:
    n = int(input('Введите результат'))
    count += 1
    if k < n:
        k = n

print(count)