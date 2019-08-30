# 클래스 vs 슬라이스

S = 'abcdef'
for x in S[::2]:
    for y in S[::2]:            # 각 반복마다 새로운 객체
        print(x + y, end=' ')

# aa ac ae ca cc ce ea ec ee


S = 'abcdef'
S = S[::2]
S
# 'ace'
for x in S:
    for y in S:                 # 동일 객체. 새로운 반복자들
        print(x + y, end=' ')

# aa ac ae ca cc ce ea ec ee
