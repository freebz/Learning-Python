# 경계에서 사용된 경우

seq = [1, 2, 3, 4]
a, b, c, *d = seq
print(a, b, c, d)
# 1 2 3 [4]


a, b, c, d, *e = seq
print(a, b, c, d, e)
# 1 2 3 4 []

a, b, *e, c, d = seq
print(a, b, c, d, e)
# 1 2 3 4 []


a, *b, c, *d = seq
# SyntaxError: two starred expressions in assignment

a, b = seq
# ValueError: too many values to unpack (expected 2)

*a = seq
# SyntaxError: starred assignment target must be in a list or tuple

*a, = seq
a
# [1, 2, 3, 4]
