# 레퍼런스 vs 복사

X = [1, 2, 3]
L = ['a', X, 'b']               # X의 객체에 대한 참조를 포함
D = {'x':X, 'y':2}


X[1] = 'surprise'               # 세 개의 모든 참조에 영향을 줌
L
# ['a', [1, 'surprise', 3], 'b']
D
# {'x': [1, 'surprise', 3], 'y': 2}


L = [1,2,3]
D = {'a':1, 'b':2}


A = L[:]                        # A = L을 대체함(또는 list(L))
B = D.copy()                    # B = D를 대체함(집합도 마찬가지)


A[1] = 'Ni'
B['c'] = 'spam'

L, D
# ([1, 2, 3], {'a': 1, 'b': 2})
A, B
# ([1, 'Ni', 3], {'a': 1, 'b': 2, 'c': 'spam'})


X = [1, 2, 3]
L = ['a', X[:], 'b']            # X의 객체에 대한 복사본을 포함
D = {'x':X[:], 'y':2}


import copy
X = copy.deepcopy(Y)            # 임의의 중첩된 객체 Y에 대한 완벽한 복사
