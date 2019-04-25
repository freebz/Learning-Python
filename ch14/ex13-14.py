# 반복 객체 range

# c:\python36\python
R = range(10)                   # range는 리스트가 아닌 반복 객체를 반환
R
# range(0, 10)

I = iter(R)                     # range 반복 객체로부터 반복자 생성
next(I)                         # 다음 결과로 전진
# 0                             # for 루프와 컴프리헨션의 내부 동작
next(I)
# 1
next(I)
# 2

list(range(10))                 # 필요한 경우 강제로 리스트 생성
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


len(R)                          # range는 len과 인덱싱 또한 지원하지만 다른 연산들은 지원하지 않음
# 10
R[0]
# 0
R[-1]
# 9

next(I)                         # .next()는 .__next__()로 변경되었지만
# 3
I.__next__()                    # 새롭게 추가된 next()를 사용하도록 하자
# 4
