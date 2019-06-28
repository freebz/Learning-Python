# 내장 타입 생성, 도구, 그리고 클래스

D = {'a':1, 'b':2, 'c':3}
x = iter(D)
next(x)
# 'a'
next(x)
# 'b'


for key in D:
    print(key, D[key])

# a 1
# b 2
# c 3


for line in open('temp.txt'):
    print(line, end='')

# Tis but
# a flesh wound.
