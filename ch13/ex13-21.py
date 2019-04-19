# 리스트 변경하기: range vs 컴프리헨션

L = [1, 2, 3, 4, 5]

for x in L:
    x += 1                      # L이 아닌 x를 변경

L
# [1, 2, 3, 4, 5]
x
# 6


L = [1, 2, 3, 4, 5]

for i in range(len(L)):         # L의 각 아이템에 1 더하기
    L[i] += 1                   # 또는 L[i] = L[i] + 1

L
# [2, 3, 4, 5, 6]


i = 0
while i < len(L):
    L[i] += 1
    i += 1

L
# [3, 4, 5, 6, 7]


[x + 1 for x in L]
