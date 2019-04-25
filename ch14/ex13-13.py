# 파이썬 3.X에서 새로운 반복 객체들

# 2.X 코드에 미치는 영향: 장점과 단점

zip('abc', 'xyz')               # 3.X에서 반복 객체(2.X에서 리스트)
# <zip object at 0x7fac26672148>

list(zip('abc', 'xyz'))         # 3.X에서 출력을 위해 강제로 결과 리스트 생성
# [('a', 'x'), ('b', 'y'), ('c', 'z')]


Z = zip((1, 2), (3, 4))         # 2.X 리스트와 달리. 인덱스 등을 사용할 수 없음
Z[0]
# TypeError: 'zip' object is not subscriptable


M = map(lambda x: 2 ** x, range(3))
for i in M: print(i)

# 1
# 2
# 4
for i in M: print(i)            # 2.X 리스트와 달리 한 번만 통과할 수 있으며, zip 또한 마찬가지
#
