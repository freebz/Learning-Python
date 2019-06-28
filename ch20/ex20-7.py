# 왜 제너레이터 함수인가?

def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res

for x in buildsquares(5): print(x, end=' : ')

# 0 : 1 : 4 : 9 : 16 :


for x in [n ** 2 for n in range(5)]:
    print(x, end=' : ')

# 0 : 1 : 4 : 9 : 16 :

for x in map((lambda n: n ** 2), range(5)):
    print(x, end=' : ')

# 0 : 1 : 4 : 9 : 16 :


def ups(line):
    for sub in line.split(','): # 부분 문자열 제너레이터
        yield sub.upper()

tuple(ups('aaa,bbb,ccc'))       # 모든 반복 상황
# ('AAA', 'BBB', 'CCC')

{i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))}
# {0: 'AAA', 1: 'BBB', 2: 'CCC'}
