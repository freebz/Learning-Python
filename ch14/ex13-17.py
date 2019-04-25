# 딕셔너리 뷰 반복 객체

D = dict(a=1, b=2, c=3)
D
# {'a': 1, 'b': 2, 'c': 3}

K = D.keys()                    # 3.X에서 리스트가 아닌 뷰 객체
K
# dict_keys(['a', 'b', 'c'])

next(K)                         # 뷰 자체는 반복자가 아님
# TypeError: 'dict_keys' object is not an iterator

I = iter(K)                     # 뷰 반복 객체는 반복자를 제공하며
next(I)                         # 반복자는 수동으로 사용될 수 있지만,
# 'a'                           # len()과 인덱싱은 지원하지 않음
next(I)
# 'b'

for k in D.keys(): print(k, end=' ') # 모든 반복 상황에서 자동으로 사용

# a b c


K = D.keys()
list(K)                         # 필요 시 강제로 실제 리스트를 생성할 수 있음
# ['a', 'b', 'c']

V = D.values()                  # values() 뷰도 items() 뷰와 마찬가지
V
# dict_values([1, 2, 3])
list(V)                         # 출력 또는 인덱싱을 위해 list()가 필요
# [1, 2, 3]

V[0]
# TypeError: 'dict_values' object does not support indexing
list(V)[0]
# 1

list(D.items())
# [('a', 1), ('b', 2), ('c', 3)]

for (k, v) in D.items(): print(k, v, end=' ')

# a 1 b 2 c 3


D                               # 딕셔너리는 여전히 반복자를 생성하며,
# {'a': 1, 'b': 2, 'c': 3}      # 반복될 때마다 다음 키를 반환함
I = iter(D)
next(I)
# 'a'
next(I)
# 'b'

for key in D: print(key, end=' ') # 여전히 반복을 위해 keys()를 호출할 필요가 없지만,
                                  # keys는 3.X에서 반복 객체
# a b c


D
# {'a': 1, 'b': 2, 'c': 3}
for k in sorted(D.keys()): print(k, D[k], end=' ')

# a 1 b 2 c 3
for k in sorted(D): print(k, D[k], end=' ') # '가장 좋은' 키 정렬 방법

# a 1 b 2 c 3
