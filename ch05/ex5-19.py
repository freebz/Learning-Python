# 집합

# 파이썬 2.6과 이전 버전에서의 집합 기초

x = set('abcde')
y = set('bdxyz')


x
# set(['b', 'a', 'd', 'e', 'c'])  # 파이썬 <= 2.6 출력 형식


x - y                           # 차집합
# set(['a', 'c', 'e'])

x | y                           # 합집합
# set(['a', 'c', 'b', 'e', 'd', 'y', 'x', 'z'])

x & y                           # 교집합
# set(['b', 'd'])

x ^ y                           # 대칭 차집합(XOR)
# set(['a', 'e', 'e', 'y', 'x', 'z'])

x > y, x < y                    # 포함 집합, 부분 집합
# (False, False)


'e' in x                        # 맴버십(집합)
# True

'e' in 'Camelot', 22 in [11, 22, 33] # 다른 타입 또한 동작함
# (True, True)


z = x.intersection(y)           # x & y와 같음
z
# set(['b', 'd'])
z.add('SPAM')                   # 아이템 하나 추가
z
# set(['b', 'd', 'SPA<'])
z.update(set(['X', 'Y']))       # 병합: 합집합
z
# set(['Y', 'X', 'b', 'd', 'SPAM'])
z.remove('b')                   # 아이템 하나 제거
z
# set(['Y', 'X', 'd', 'SPAM'])


for item in set('abc'): print(item * 3)

# aaa
# ccc
# bbb


S = set([1, 2, 3])
S | set([3, 4])                 # 표현식에는 피연산자가 모두 집합이어야 함
# set([1, 2, 3, 4])
S | [3, 4]
# TypeError: unsupported operand type(s) for |: 'set' and 'list'

S.union([3, 4])                 # 하지만 메서드에서는 반복 가능한 다른 타입도 가능함
# set([1, 2, 3, 4])
S.intersection((1, 3, 5))
# set([1, 3])
S.issubset(range(-5, 5))
# True
