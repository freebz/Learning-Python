# 다자간 분기 스위치

key = 'got'
{'already': (lambda: 2 + 2),
 'got':     (lambda: 2 * 4),
 'one':     (lambda: 2 ** 6)}[key]()
# 8


def f1(): return 2 + 2

def f2(): return 2 * 4

def f3(): return 2 ** 6

key = 'one'
{'already': f1, 'got': f2, 'one': f3}[key]()
