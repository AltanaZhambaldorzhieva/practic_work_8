income = float(input())
k = 0
total = income

while income != 0:
    income = float(input())
    k += 1
    total += income

print(total/k)