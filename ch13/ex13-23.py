# 파이썬 2.X에서 map

S1 = 'abc'
S2 = 'xyz123'

map(None, S1, S2)               # 2.X에서만 동작: 긴 시퀀스를 기준으로 채움
# [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]


list(map(ord, 'spam'))
# [115, 112, 97, 109]


res = []
for c in 'spam': res.append(ord(c))
res
# [115, 112, 97, 109]
