# 키워드 전용 인수 사용하기

#!python3
"3.X의 키워드 전용 인수만 사용"
import sys

def print3(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print3(99, name='bob')
# TypeError: print3() got an unexpected keyword argument 'name'
