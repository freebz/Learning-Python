# 다수 vs 단일 패스 반복자

R = range(3)                    # range는 다수의 반복자를 허용함
next(R)
# TypeError: 'range' object is not an iterator

I1 = iter(R)
next(I1)
# 0
next(I1)
# 1
I2 = iter(R)                    # 하나의 range에 두 개의 반복자
next(I2)
# 0
next(I1)                        # I1은 I2와 다른 지점에 있음
# 2


Z = zip((1, 2, 3), (10, 20, 30))
I1 = iter(Z)
I2 = iter(Z)                    # zip에 대한 두 개의 반복자
next(I1)
# (1, 10)
next(I1)
# (2, 20)
next(I2)                        # (3.X) I2는 I1과 같은 위치
# (3, 30)

M = map(abs, (-1, 0, 1))        # map과 filter도 동일
I1 = iter(M); I2 = iter(M)
print(next(I1), next(I1), next(I1))
# 1 0 1
next(I2)                        # (3.X) 한 번만 탐색할 수 있음
# StopIteration

R = range(3)                    # 그러나 range는 다수 반복자를 허용함
I1, I2 = iter(R), iter(R)
[next(I1), next(I1), next(I1)]
# [0, 1, 2]
next(I2)                        # 2.X 리스트처럼 다수의 탐색
# 0
