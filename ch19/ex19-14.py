# 파이썬 코드를 복잡하게 하는 방법

if a:
    b
else:
    c


b if a else c
((a and b) or c)


lower = (lambda x, y: x if x < y else y)
lower('bb', 'aa')
# 'aa'
lower('aa', 'bb')
# 'aa'


import sys
showall = lambda x: list(map(sys.stdout.write, x)) # 3.X에서 list를 사용해야 함
t = showall(['spam\n', 'toast\n', 'eggs\n'])       # 3.X에서 print 사용할 수 있음
# spam
# toast
# eggs
showall = lambda x: [sys.stdout.write(line) for line in x]
t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))
# bright
# side
# of
# life
showall = lambda x: [print(line, end='') for line in x] # 동일: 3.X에서만
showall = lambda x: print(*x, sep='', end='')           # 동일: 3.X에서만
