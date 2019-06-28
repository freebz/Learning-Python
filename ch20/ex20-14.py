# 확장으로부터의 파이썬 3.3 yield

def both(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)): yield i

list(both(5))
# [0, 1, 2, 3, 4, 0, 1, 4, 9, 16]


def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))

list(both(5))
# [0, 1, 2, 3, 4, 0, 1, 4, 9, 16]

' : '.join(str(i) for i in both(5))
# '0 : 1 : 2 : 3 : 4 : 0 : 1 : 4 : 9 : 16'
