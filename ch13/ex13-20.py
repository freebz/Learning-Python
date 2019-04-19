# 완전하지 않은 순회: range vs 슬라이스

S = 'abcdefghijk'
list(range(0, len(S), 2))
# [0, 2, 4, 6, 8, 10]

for i in range(0, len(S), 2): print(S[i], end=' ')

# a c e g i k


S = 'abcdefghijk'
for c in S[::2]: print(c, end=' ')

# a c e g i k
