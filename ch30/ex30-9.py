# 단일 스캔 vs 다중 스캔

X = Squares(1, 5)               # 상태 정보를 갖는 반복 객체 생성
[n for n in X]                  # 아이템을 모두 훑음: __iter__는 self를 반환
# [1, 4, 9, 16, 25]
[n for n in X]                  # 이제 빈 상태: __iter__는 동일한 self를 반환
# []
[n for n in Squares(1, 5)]      # 새로운 반복 객체 생성
# [1, 4, 9, 16, 25]
list(Squares(1, 3))             # 각 새로운 __iter__ 호출을 위한 새로운 객체
# [1, 4, 9]


36 in Squares(1, 10)            # 다른 반복 맥락
# True
a, b, c = Squares(1, 3)         # 각각은 __iter__를 호출한 뒤, __next__를 호출
a, b, c
# (1, 4, 9}
':'.join(map(str, Squares(1, 5)))
# '1:4:9:16:25'


X = Squares(1, 5)
tuple(X), tuple(X)              # 반복자는 두 번째 tuple()에서 모두 고갈된 상태
# ((1, 4, 9, 16, 25), ())

X = list(Squares(1, 5))
tuple(X), tuple(X)
