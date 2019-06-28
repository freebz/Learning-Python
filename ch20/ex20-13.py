# 제너레이터는 단일 반복 객체

G = (c * 4 for c in 'SPAM')
iter(G) is G                    # 나 자신이 반복자임. G는 __next__를 제공함
# True


G = (c * 4 for c in 'SPAM')     # 새로운 제너레이터 생성
I1 = iter(G)                    # 수동으로 반복
next(I1)
# 'SSSS'
next(I1)
# 'PPPP'
I2 = iter(G)                    # 같은 위치를 가리키는 두 번째 반복자
next(I2)
# 'AAAA'


list(I1)                        # I1의 모든 아이템을 가져옴
# ['MMMM']
next(I2)                        # 다른 반복자 또한 소모됨
# StopIteration

I3 = iter(G)                    # 새로운 반복자 또한 소모됨
next(I3)
# StopIteration

I3 = iter(c * 4 for c in 'SPAM') # 다시 시작하기 위한 새로운 제너레이터
next(I3)
# 'SSSS'


def timesfour(S):
    for c in S:
        yield c *4

G = timesfour('spam')           # 제너레이터 함수도 동일하게 동작함
iter(G) is G
# True
I1, I2 = iter(G), iter(G)
next(I1)
# 'ssss'
next(I1)
# 'pppp'
next(I2)
# 'aaaa'


L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)
next(I1)
# 1
next(I1)
# 2
next(I2)                        # 리스트는 다수의 반복자를 지원함
# 1
del L[2:]                       # 변경된 내용이 반복자에 반영되었음
next(I1)
# StopIteration
