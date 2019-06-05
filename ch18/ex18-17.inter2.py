# 일반화된 집합 함수들

def intersect(*args):
    res = []
    for x in args[0]:                   # 첫 번째 시퀀스 탐색
        if x in res: continue           # 중복 항목은 건너뜀
        for other in args[1:]:          # 다른 인수들을 위하여
            if x not in other: break    # 각각의 인수에 해당 항목이 있는지?
        else:                           # 없으면: 루프 빠져나가기
            res.append(x)               # 있으면: 마지막에 항목 추가
    return res

def union(*args):
    res = []
    for seq in args:                    # 모든 인수를 위해
        for x in seq:                   # 모든 항목을 위해
            if not x in res:
                res.append(x)           # 새로운 항목을 결과에 추가
    return res


# % python
from iter2 import intersect, union
s1, s2, s3 = "SPAM", "SCAM", "SLAM"

intersect(s1, s2), union(s1, s2) # 두 개의 피연산자
# (['S', 'A', 'M'], ['S', 'P', 'A', 'M', 'C'])

intersect([1, 2, 3], (1, 4))    # 혼합된 타입들
# [1]

intersect(s1, s2, s3)           # 세 개의 피연산자
# ['S', 'A', 'M']

union(s1, s2, s3)
# ['S', 'P', 'A', 'M', 'C', 'L']


def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))

tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
# ('abcdefg', 'abdst', 'albmcnd', 'a')
# ['a']
# ('abdst', 'albmcnd', 'a', 'abcdefg')
# ['a']
# ('albmcnd', 'a', 'abcdefg', 'abdst')
# ['a']
# ('a', 'abcdefg', 'abdst', 'albmcnd')
# ['a']

tester(union, ('a', 'abcdefg', 'abdst', 'albmcnd'), False)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 's', 't']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 's', 't']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 's', 't']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 's', 't']

tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmcnd'), False)
# ['a', 'b']
# ['a', 'b']
# ['a', 'b']
# ['a', 'b']


intersect([1, 2, 1, 3], (1, 1, 4))
# [1]
union([1, 2, 1, 3], (1, 1, 4))
# [1, 2, 3, 4]
tester(intersect, ('ababa', 'abcdefga', 'aaaab'), False)
# ['a', 'b']
# ['a', 'b']
# ['a', 'b']


def tester(func, items, trace=True):
    for args in scramble(items):
        ...인수들 사용하기...
