# 클래스 vs 제너레이터

def gsquares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2

for i in gsquares(1, 5):
    print(i, end=' ')

# 1 4 9 16 25

for i in (x ** 2 for x in range(1, 6)):
    print(i, end=' ')

# 1 4 9 16 25


[x ** 2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]
