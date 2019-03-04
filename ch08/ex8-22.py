# 딕셔너리 뷰와 집합

K, V
# (dict_keys(['a', 'c']), dict_values([1, 3]))

K | {'x': 4}                    # 키 뷰는 집합과 유사함
# {'x', 'c', 'a'}

V & {'x': 4}
# TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict'
V & {'x': 4}.values()
# TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict_values'


D = {'a': 1, 'b': 2, 'c': 3}
D.keys() & D.keys()             # 키 뷰들의 교집합
# {'b', 'c', 'a'}
D.keys() & {'b'}                # 키와 집합의 교집합
# {'b'}
D.keys() & {'b': 1}             # 키와 딕셔너리의 교집합
# {'b'}
D.keys() | {'b', 'c', 'd'}      # 키와 집합의 합집합
# {'c', 'a', 'b', 'd'}


D = {'a': 1}
list(D.items())                 # 해시 가능한 경우 아이템들의 뷰는 집합과 같음
# [('a', 1)]
D.items() | D.keys()            # 뷰와 뷰의 합집합
# {'a', ('a', 1)}
D.items() | D                   # 딕셔너리는 자신의 키와 동일하게 취급됨
# {'a', ('a', 1)}

D.items() | {('c', 3), ('d', 4)} # 키/값 쌍의 집합
# {('c', 3), ('d', 4), ('a', 1)}

dict(D.items() | {('c', 3), ('d', 4)}) # dict는 반복 가능한 집합 또는 받아들임
# {'c': 3, 'd': 4, 'a': 1}
