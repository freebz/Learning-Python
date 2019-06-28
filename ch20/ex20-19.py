# 예제: 뒤섞인 시퀀스 생성하기

# 시퀀스 뒤섞기

L, S = [1, 2, 3], 'spam'
for i in range(len(S)):         # 0..3 카운트 반복을 위해
    S = S[1:] + S[:1]           # 앞 쪽 아이템을 마지막으로 이동
    print(S, end=' ')

# pams amsp mspa spam


for i in range(len(L)):
    L = L[1:] + L[:1]           # 슬라이스를 사용하기 때문에
    print(L, end=' ')           # 모든 시퀀스 타입에 대해 동작함

# [2, 3, 1] [3, 1, 2] [1, 2, 3]


for i in range(len(S)):         # 0..3 위치를 위해
    X = S[i:] + S[:i]           # 뒷부분 + 앞부분(동일한 효과)
    print(X, end=' ')

# spam pams amsp mspa
