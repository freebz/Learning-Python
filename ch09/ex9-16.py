# 파이썬 2.X 그리고 3.X에서 혼합된 타입 비교와 정렬

# c:\python27\python
11 == '11'                      # 동등 비교는 비숫자를 변환하지 않음
# False
11 >= '11'                      # 2.X는 타입 이름 문자열로 비교: int, str
# False
['11', '22'].sort()             # 정렬의 경우도 마찬가지
[11, '11'].sort()


# c:\python36\python
11 == '11'                      # 3.X: 동등 비교는 동작하지만, 크기 비교는 동작하지 않음
# False
11 >= '11'
# TypeError: unorderable types: int() > str()

['11', '22'].sort()             # 정렬의 경우도 마찬가지
[11, '11'].sort()
# TypeError: unorderable types: str() < int()

11 > 9.123                      # 혼합된 숫자는 가장 높은 유형으로 변환
# True
str(11) >= '11', 11 >= int('11') # 문제를 해결하기 위한 수동 변환
# (True, True)
