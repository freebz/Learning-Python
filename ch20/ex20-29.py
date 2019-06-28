# 더 생각해 볼 주제: 일회성 반복

def myzip(*args):
    iters = map(iter, args)
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)


list(myzip('abc', 'lmnop'))
# [('a', 'l'), ('b', 'm'), ('c', 'n')]


def myzip(*args):
    iters = list(map(iter, args)) # 여러 번 탐색 가능
    ...나머지는 그대로...
