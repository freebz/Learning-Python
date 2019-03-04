# 3.X에서의(그리고 2.7에서 새로운 메서드를 통한) 딕셔너리 뷰

D = dict(a=1, b=2, c=3)
D
# {'a': 1, 'b': 2, 'c': 3}

K = D.keys()                    # 3.X에서 리스트가아닌 뷰 객체 생성
K
# dict_keys(['a', 'b', 'c'])
list(K)                         # 필요한 경우 강제로 리스트로 변환
# ['a', 'b', 'c']

V = D.values()                  # 결과 아이템 뷰에 대해 위와 같은 방법
V
# dict_values([1, 2, 3])
list(V)
# [1, 2, 3]

D.items()
# dict_items([('a', 1), ('b', 2), ('c', 3)])
list(D.items())
# [('a', 1), ('b', 2), ('c', 3)]

K[0]                            # 변환 없이 리스트 연산을 수행하면 실패함
# TypeError: 'dict_keys' object does not support indexing
list(K)[0]
# 'a'


for k in D.keys(): print(k)     # 루프에서 자동으로 반복자(iterator)가 사용됨

# a
# b
# c


for key in D: print(key)        #  반복을 위해 여전히 keys()를 호출할 필요는 없음

# a
# b
# c


D = {'a': 1, 'b': 2, 'c': 3}
D
# {'a': 1, 'b': 2, 'c': 3}

K = D.keys()
V = D.values()
list(K)                         # 뷰는 딕셔너리와 같은 순서를 유지함
# ['a', 'b', 'c']
list(V)
# [1, 2, 3]

del D['b']                      # 딕셔너리를 직접 변경
D
# {'a': 1, 'c': 3}

list(K)                         # 현재 생성되어 있는 모든 뷰 객체에 반영됨
# ['a', 'c']
list(V)                         # 2.X에서는 결과가 다르다! 딕셔너리에서 분리된 리스트
# [1, 3]
