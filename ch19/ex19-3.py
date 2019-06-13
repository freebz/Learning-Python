# 반복문 vs 재귀

L = [1, 2, 3, 4, 5]
sum = 0
while L:
    sum += L[0]
    L = L[1:]
sum
# 15


L = [1, 2, 3, 4, 5]
sum = 0
for x in L: sum += x

sum
# 15
