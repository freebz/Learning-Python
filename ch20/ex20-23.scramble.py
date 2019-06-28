# 테스터 클라이언트

# file scramble.py

def scramble(seq):
    for i in range(len(seq)):   # 제너레이터 함수는
        yield seq[i:] + seq[:i] # 반복마다 하나의 아이템을 산출함

scramble2 = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))


from scramble import scramble
from inter2 import intersect, union

def tester(func, items, trace=True):
    for args in scramble(items): # 제너레이터 사용(또는 scramble2(items))
        if trace: print(args)
        print(sorted(func(*args)))

tester(intersect, ('aab', 'abcde', 'ababab'))
# ('aab', 'abcde', 'ababab')
# ['a', 'b']
# ('abcde', 'ababab', 'aab')
# ['a', 'b']
# ('ababab', 'aab', 'abcde')
# ['a', 'b']

tester(intersect, ([1, 2], [2, 3, 4], [1, 6, 2, 7, 3]), False)
# [2]
# [2]
# [2]
