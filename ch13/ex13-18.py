# 시퀀스 탐색: while과 range vs for

X = 'spam'
for item in X: print(item, end=' ') # 단순한 반복

# s p a m


i = 0
while i < len(X):               # while 루프 반복
    print(X[i], end=' ')
    i += 1

# s p a m


X
# 'spam'
len(X)                          # 문자열의 길이
# 4
list(range(len(X)))             # X에 대한 모든 유효한 오프셋
# [0, 1, 2, 3]

for i in range(len(X)): print(X[i], end=' ') # 수동 range/len 반복

# s p a m


for item in X: print(item, end=' ') # 가능한 단순한 반복을 사용하자
