# 변환, 메서드 그리고 불변성

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)                   # 튜플의 아이템들로부터 리스트를 만듦
tmp.sort()                      # 리스트 정렬
tmp
# ['aa', 'bb', 'cc', 'dd']
T = tuple(tmp)                  # 리스트의 아이템들로부터 튜플을 만듦
T
# ('aa', 'bb', 'cc', 'dd')

sorted(T)                       # 또는 내장 sorted를 사용하고 저장하는 두 단계
# ['aa', 'bb', 'cc', 'dd']


T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]
L
# [21, 22, 23, 24, 25]


T = (1, 2, 3, 2, 4, 2)          # 2.6, 3.0 그리고 이후 버전에서 튜플 메서드들
T.index(2)                      # 2가 처음 위치한 오프셋
# 1
T.index(2, 2)                   # 오프셋 2 이후에 위치한 2의 오프셋
# 3
T.count(2)                      # 몇 개의 2가 있는가?
# 3


T = (1, [2, 3], 4)
T[1] = 'spam'                   # 실패: 튜플 자체를 변경할 수는 없음
# TypeError: 'tuple' object does not support item assignment

T[1][0] = 'spam'                # 성공: 내부에 있는 가변 객체는 수정할 수 있음
T
# (1, ['spam', 3], 4)
