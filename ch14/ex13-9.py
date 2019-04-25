# 파일에 리스트 컴프리헨션 사용하기

f = open('script2.py')
lines = f.readlines()
lines
# ['import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n']


lines = [line.rstrip() for line in lines]
lines
# ['import sys', 'print(sys.path)', 'x = 2', 'print(x ** 32)']


lines = [line.rstrip() for line in open('script2.py')]
lines
# ['import sys', 'print(sys.path)', 'x = 2', 'print(x ** 32)']


[line.upper() for line in open('script2.py')]
# ['IMPORT SYS\n', 'PRINT(SYS.PATH)\n', 'X = 2\n', 'PRINT(X ** 32)\n']

[line.rstrip().upper() for line in open('script2.py')]
# ['IMPORT SYS', 'PRINT(SYS.PATH)', 'X = 2', 'PRINT(X ** 32)']

[line.split() for line in open('script2.py')]
# [['import', 'sys'], ['print(sys.path)'], ['x', '=', '2'], ['print(x', '**', '32)']]

[line.replace(' ', '!') for line in open('script2.py')]
# ['import!sys\n', 'print(sys.path)\n', 'x!=!2\n', 'print(x!**!32)\n']

[('sys' in line, line[:5]) for line in open('script2.py')]
# [(True, 'impor'), (True, 'print'), (False, 'x = 2'), (False, 'print')]
