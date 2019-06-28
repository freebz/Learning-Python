# 제너레이터 표현식

S
# 'spam'
G = (S[i:] + S[:i] for i in range(len(S))) # 동등한 제너레이터 표현식
list(G)
# ['spam', 'pams', 'amsp', 'mspa']


F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
F(S)
# <generator object <lambda>.<locals>.<genexpr> at 0x7ff6b6ebe360>

list(F(S))
# ['spam', 'pams', 'amsp', 'mspa']
list(F([1, 2, 3]))
# [[1, 2, 3], [2, 3, 1], [3, 1, 2]]

for x in F((1, 2, 3)):
    print(x, end=' ')

# (1, 2, 3) (2, 3, 1) (3, 1, 2)
