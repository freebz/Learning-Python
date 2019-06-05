#!python
"""
2.X(와 3.X)에서 사용할 수 있는 3.X print 함수의 대부분의 기능을 흉내 냄
호출식: print3(*args, sep=' ', end='\n', file=sys.stdout)
"""
import sys

def print3(*args, **kargs):
    sep = kargs.get('sep', ' ') # 키워드 인수 기본값
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
