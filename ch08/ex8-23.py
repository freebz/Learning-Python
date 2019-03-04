# 3.X에서 딕셔너리 키 정렬

D = {'a': 1, 'b': 2, 'c': 3}
D
# {'a': 1, 'b': 2, 'c': 3}

Ks = D.keys()                   # 뷰 객체에 대한 정렬은 동작하지 않음!
Ks.sort()
# AttributeError: 'dict_keys' object has no attribute 'sort'


Ks = list(Ks)                   # 강제로 리스트로 변환한 다음 정렬
Ks.sort()
for k in Ks: print(k, D[k])     # 2.X: print의 외부 괄호 생략

# a 1
# b 2
# c 3

D
# {'a': 1, 'b': 2, 'c': 3}
Ks = D.keys()                       # 또는 키에 대해 sorted()를 사용할 수 있음
for k in sorted(Ks): print(k, D[k]) # sorted()는 모든 가변 객체를 허용함
                                    # sorted() 정렬된 결과를 반환함
# a 1
# b 2
# c 3


D
# {'a': 1, 'b': 2, 'c': 3}         # 하지만 딕션너리를 직접 정렬하는 것이 더 나음
for k in sorted(D): print(k, D[k]) # 딕셔너리 반복자는 키들을 반환함

# a 1
# b 2
# c 3
