# 파이썬 3.X에서 확장된 시퀀스 언패킹

# 확장된 언패킹의 실제 동작

# c:\python36\python
seq = [1, 2, 3, 4]

a, b, c, d = seq
print(a, b, c, d)
# 1 2 3 4

a, b = seq
# ValueError: too many values to unpack (expected 2)


a, *b = seq
a
# 1
b
# [2, 3, 4]


*a, b = seq
a
# [1, 2, 3]
b
# 4


a, *b, c = seq
a
# 1
b
# [2, 3]
c
# 4


a, b, *c = seq
a
# 1
b
# 2
c
# [3, 4]


a, *b = 'spam'
a, b
# ('s', ['p', 'a', 'm'])

a, *b, c = 'spam'
a, b, c
# ('s', ['p', 'a'], 'm')

a, *b, c = range(4)
a, b, c
# (0, [1, 2], 3)


S = 'spam'

S[0], S[1:]                     # 슬라이스는 타입에 따라 다르지만, * 할당은 항상 리스트로 반환
# ('s', 'pam')

S[0], S[1:3], S[3]
# ('s', 'pa', 'm')


L = [1, 2, 3, 4]
while L:
    front, *L = L               # 슬라이싱 없이 첫 번째와 나머지 아이템 구하기
    print(front, L)

# 1 [2, 3, 4]
# 2 [3, 4]
# 3 [4]
# 4 []
