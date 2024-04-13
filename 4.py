k = int(input())
summ = 0
ans = []
for i in range(0, k + 1):
    summ += i
    ans.append(summ)
for j in range(0, len(ans) + 1):
    m = ans[j + 1]
    print(m)



