# 다른 반복 상황들

for line in open('script2.py'):    # 파일 반복자 사용
    print(line.upper(), end='')

# IMPORT SYS
# PRINT(SYS.PATH)
# X = 2
# PRINT(X ** 32)


uppers = [line.upper() for line in open('script2.py')]
uppers
# ['IMPORT SYS\n', 'PRINT(SYS.PATH)\n', 'X = 2\n', 'PRINT(X ** 32)\n']

map(str.upper, open('script2.py'))            # 3.X에서 map은 반복 객체
# <map object at 0x7fac2666e278>
list(map(str.upper, open('script2.py')))
# ['IMPORT SYS\n', 'PRINT(SYS.PATH)\n', 'X = 2\n', 'PRINT(X ** 32)\n']


sorted(open('script2.py'))
# ['import sys\n', 'print(sys.path)\n', 'print(x ** 32)\n', 'x = 2\n']

list(zip(open('script2.py'), open('script2.py')))
# [('import sys\n', 'import sys\n'), ('print(sys.path)\n', 'print(sys.path)\n'), ('x = 2\n', 'x = 2\n'), ('print(x ** 32)\n', 'print(x ** 32)\n')]

list(enumerate(open('script2.py')))
# [(0, 'import sys\n'), (1, 'print(sys.path)\n'), (2, 'x = 2\n'), (3, 'print(x ** 32)\n')]

list(filter(bool, open('script2.py')))     # 비어 있지 않은 경우 = True
# ['import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n']

import functools, operator
functools.reduce(operator.add, open('script2.py'))
# 'import sys\nprint(sys.path)\nx = 2\nprint(x ** 32)\n'


list(open('script2.py'))
# ['import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n']

tuple(open('script2.py'))
# ('import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n')

'&&'.join(open('script2.py'))
# 'import sys\n&&print(sys.path)\n&&x = 2\n&&print(x ** 32)\n'


a, b, c, d = open('script2.py')           # 시퀀스 할당
a, b
# ('import sys\n', 'print(sys.path)\n')

a, *b = open('script2.py')                # 3.X 확장 형식
a, b
# ('import sys\n', ['print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n'])

'y = 2\n' in open('script2.py')           # 멤버십 테스트
# False
'x = 2\n' in open('script2.py')
# True

L = [11, 22, 33, 44]                      # 슬라이스 할당
L[1:3] = open('script2.py')
L
# [11, 'import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n', 44]

L = [11]
L.extend(open('script2.py'))              # list.extend 메서드
L
# [11, 'import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n']


L = [11]
L.append(open('script2.py'))              # list.append는 바복하지 않음
L
# [11, <_io.TextIOWrapper name='script2.py' mode='r' encoding='UTF-8'>]
list(L[1])
# ['import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n']


set(open('script2.py'))
# {'import sys\n', 'print(x ** 32)\n', 'x = 2\n', 'print(sys.path)\n'}

{line for line in open('script2.py')}
# {'import sys\n', 'print(x ** 32)\n', 'x = 2\n', 'print(sys.path)\n'}

{ix: line for ix, line in enumerate(open('script2.py'))}
# {0: 'import sys\n', 1: 'print(sys.path)\n', 2: 'x = 2\n', 3: 'print(x ** 32)\n'}


{line for line in open('script2.py') if line[0] == 'p'}
# {'print(x ** 32)\n', 'print(sys.path)\n'}
{ix: line for (ix, line) in enumerate(open('script2.py')) if line[0] == 'p'}
# {1: 'print(sys.path)\n', 3: 'print(x ** 32)\n'}


list(line.upper() for line in open('script2.py'))    # 20장 참조
# ['IMPORT SYS\n', 'PRINT(SYS.PATH)\n', 'X = 2\n', 'PRINT(X ** 32)\n']


sum([3, 2, 4, 1, 5, 0])         # sum은 숫자에 대해서만 동작
# 15
any(['spam', '', 'ni'])
# True
all(['spam', '', 'ni'])
# False
max([3, 2, 5, 1, 4])
# 5
min([3, 2, 5, 1, 4])
# 1


max(open('script2.py'))         # 최대/최소 문자열 라인
# 'x = 2\n'
min(open('script2.py'))
# 'import sys\n'


def f(a, b, c, d): print(a, b, c, d, sep='&')

f(1, 2, 3, 4)
# 1&2&3&4
f(*[1, 2, 3, 4])                # 인수들로 풀기
# 1&2&3&4

f(*open('script2.py'))          # 라인들을 반복
# import sys
# &print(sys.path)
# &x = 2
# &print(x ** 32)


X = (1, 2)
Y = (3, 4)

list(zip(X, Y))                 # 튜플 묶기: 반복 객체 반환
# [(1, 3), (2, 4)]

A, B = zip(*zip(X, Y))          # zip으로 묶인 것 풀기!
A
# (1, 2)
B
# (3, 4)
