n = int(input())
k = 0
for i in range(2, n+1):
    nice = 0
    for j in range(1, n+1):
        if i % j == 0:
            nice += j
    if nice == 2*i:
        k += 1
print(k)
