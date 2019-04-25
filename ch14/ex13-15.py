# map, zip, filter 반복 객체

M = map(abs, (-1 ,0, 1))        # map은 리스트가 아닌 반복 객체를 반환
M
# <map object at 0x7fac2666e828>
next(M)                         # 반복자를 수동으로 사용: 결과를 소모함
# 1                             # len() 또는 인덱싱은 지원되지 않음
next(M)
# 0
next(M)
# 1
next(M)
# StopIteration

for x in M: print(x)            # 여기서 map 반복자는 비어 있음: 한 번만 반복 가능

#
M = map(abs, (-1, 0, 1))        # 재탐색을 위해 새로운 반복 객체/반복자 생성
for x in M: print(x)            # 반복 상황은 next()를 자동으로 호출

# 1
# 0
# 1
list(map(abs, (-1, 0, 1)))      # 필요한 경우 실제 리스트를 구할 수 있음
# [1, 0, 1]


Z = zip((1, 2, 3), (10, 20, 30)) # zip도 마찬가지로 한 번만 반복 가능
Z
# <zip object at 0x7fac26672188>

list(Z)
# [(1, 10), (2, 20), (3, 30)]

for pair in Z: print(pair)      # 한 번 반복하면 소모됨

#
Z = zip((1, 2, 3), (10, 20, 30))
for pair in Z: print(pair)      # 반복자는 수동 또는 자동으로 사용됨

# (1, 10)
# (2, 20)
# (3, 30)

Z = zip((1, 2, 3), (10, 20, 30)) # 수동 반복(iter()가 필요하지 않음)
next(Z)
# (1, 10)
next(Z)
# (2, 20)


filter(bool, ['spam', '', 'ni'])
# <filter object at 0x7fac2666e128>
list(filter(bool, ['spam', '', 'ni']))
# ['spam', 'ni']


[x for x in ['spam', '', 'ni'] if bool(x)]
# ['spam', 'ni']
[x for x in ['spam', '', 'ni'] if x]
# ['spam', 'ni']
