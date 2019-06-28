# 예제: 리스트 컴프리헨션 그리고 행렬

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]


M[1]                            # 2행
# [4, 5, 6]

M[1][2]                         # 2행 세 번째 아이템
# 6


[row[1] for row in M]           # 두 번째 열
# [2, 5, 8]

[M[row][1] for row in (0, 1, 2)] # 오프셋 사용
# [2, 5, 8]


[M[i][i] for i in range(len(M))] # 대각선
# [1, 5, 9]
[M[i][len(M)-1-i] for i in range(len(M))]
# [3, 5, 7]


L = [[1, 2, 3], [4, 5, 6]]
for i in range(len(L)):
    for j in range(len(L[i])):  # 직접 업데이트
        L[i][j] += 10

L
# [[11, 12, 13], [14, 15, 16]]


[col + 10 for row in M for col in row] # 새로운 값을 유지하고자 할 경우 다시 M에 할당
# [11, 12, 13, 14, 15, 16, 17, 18, 19]

[[col + 10 for col in row] for row in M]
# [[11, 12, 13], [14, 15, 16], [17, 18, 19]]


res = []
for row in M:                   # 문을 이용한 같은 기능
    for col in row:             # 오른쪽 부분을 더 들여씀
        res.append(col + 10)

res
# [11, 12, 13, 14, 15, 16, 17, 18, 19]

res = []
for row in M:
    tmp = []                    # 왼쪽 중첩은 새로운 리스트를 시작
    for col in row:
        tmp.append(col +10)
    res.append(tmp)

res
# [[11, 12, 13], [14, 15, 16], [17, 18, 19]]


M
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N
# [[2, 2, 2], [3, 3, 3], [4, 4, 4]]

[M[row][col] * N[row][col] for row in range(3) for col in range(3)]
# [2, 4, 6, 12, 15, 18, 28, 32, 36]

[[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
# [[2, 4, 6], [12, 15, 18], [28, 32, 36]]


res =[]
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(M[row][col] * N[row][col])
    res.append(tmp)


[[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(M, N)]

res = []
for (row1, row2) in zip(M, N):
    tmp = []
    for (col1, col2) in zip(row1, row2):
        tmp.append(col1 * col2)
    res.append(tmp)
