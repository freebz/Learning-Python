# 오프셋과 아이템 모두 생성하기: enumerate

S = 'spam'
offset = 0
for item in S:
    print(item, 'appears at offset', offset)
    offset += 1

# s appears at offset 0
# p appears at offset 1
# a appears at offset 2
# m appears at offset 3


S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)

# s appears at offset 0
# p appears at offset 1
# a appears at offset 2
# m appears at offset 3


E = enumerate(S)
E
# <enumerate object at 0x7f4080608048>
next(E)
# (0, 's')
next(E)
# (1, 'p')
next(E)
# (2, 'a')


[c * i for (i, c) in enumerate(S)]
# ['', 'p', 'aa', 'mmm']

for (i, l) in enumerate(open('test.txt')):
    print('%s) %s' % (i, l.rstrip()))

# 0) aaaaaa
# 1) bbbbbb
# 2) cccccc
