# 컴프리헨션

col2 = [row[1] for row in M]    # 두 번째 열 아이템만 뽑아냄
col2
# [2, 5, 8]

M                               # 행렬 자체는 변경되지 않음
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


[row[1] + 1 for row in M]       # 2열의 각 아이템에 1 더하기
# [3, 6, 9]

[row[1] for row in M if row[1] % 2 == 0] # 홀수 아이템 필터링
# [2, 8]


diag = [M[i][i] for i in [0, 1, 2]] # 행렬에서 대각선 값을 가져옴
diag
# [1, 5, 9]

doubles = [c * 2 for c in 'spam'] # 문자열에 있는 문자들을 반복
doubles
# ['ss', 'pp', 'aa', 'mm']


list(range(4))                  # 0..3(파이썬 3.X에서 list() 필요)
# [0, 1, 2, 3]
list(range(-6, 7, 2))           # -6에서 +6까지 2씩(파이썬 3.X에서 list() 필요)
# [-6, -4, -2, 0, 2, 4, 6]

[[x ** 2, x ** 3] for x in range(4)] # 다수의 값. "if" 필터
# [[0, 0], [1, 1], [4, 8], [9, 27]]
[[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]
# [[2, 1.0, 4], [4, 2.0, 8], [6, 3.0, 12]]


G = (sum(row) for row in M)     # 행의 합을 반환하는 제너레이터 생성
next(G)                         # iter(G)를 사용할 필요 없음
# 6
next(G)                         # 반복 프로토콜 next() 실행
# 15
next(G)
# 24


list(map(sum, M))               # map은 M에 있는 아이템의 합을 구함
# [6, 15, 24]


{sum(row) for row in M}         # 행의 합에 대한 집합 생성
# {24, 6, 15}

{i : sum(M[i]) for i in range(3)} # 행의 합에 대한 키/값 테이블 생성
# {0: 6, 1: 15, 2: 24}


[ord(x) for x in 'spaam']       # 각 문자의 숫자 값들의 리스트
# [115, 112, 97, 97, 109]
{ord(x) for x in 'spaam'}       # 집합은 중복을 제거
# {112, 97, 115, 109}
{x: ord(x) for x in 'spaam'}    # 딕셔너리에서 키는 유일한 값
# {'s': 115, 'p': 112, 'a': 97, 'm': 109}
(ord(x) for x in 'spaam')       # 숫자 값들의 제너레이터
# <generator object <genexpr> at 0x7f6ad4802a40>
