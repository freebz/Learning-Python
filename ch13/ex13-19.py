# 시퀀스 뒤섞기: range과 len

S = 'spam'
for i in range(len(S)):         # 반복 카운트에 대한 0..3
    S = S[1:] + S[:1]           # 제일 앞 아이템으로 끝으로 이동
    print(S, end=' ')

# pams amsp mspa spam

S
# 'spam'
for i in range(len(S)):         # 위치에 대한 0..3
    X = S[i:] + S[:i]           # 뒷부분 + 앞부분
    print(X, end=' ')
# spam pams amsp mspa


L = [1, 2, 3]
for i in range(len(L)):         # 임의의 시퀀스 타입에 대해 동작
    X = L[i:] + L[:i]
    print(X, end=' ')

# [1, 2, 3] [2, 3, 1] [3, 1, 2]
