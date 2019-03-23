# 파이썬 2.X 그리고 3.X에서 딕셔너리 비교

# c:\python27\python
D1 = {'a':1, 'b':2}
D2 = {'a':1, 'b':3}
D1 == D2                        # 딕셔너리 동등 비교: 2.X + 3.X
# False
D1 < D2                         # 딕셔너리 크기 비교: 2.X만 지원
# True


# c:\python36\python
D1 = {'a':1, 'b':2}
D2 = {'a':1, 'b':3}
D1 == D2
# False
D1 < D2
# TypeError: unorderable types: dict() < dict()


list(D1.items())
# [('a', 1), ('b', 2)]
sorted(D1.items())
# [('a', 1), ('b', 2)]

sorted(D1.items()) < sorted(D2.items()) # 3.X에서 크기 비교
# True
sorted(D1.items()) > sorted(D2.items())
# False
