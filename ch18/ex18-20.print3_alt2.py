#!python
"기본값과 함께 2.X/3.X 키워드 인수 삭제 사용"
import sys

def print3(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs: raise TyepError('extra keywords: %s' % kargs)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print3(99, name='bob')
# NameError: name 'TyepError' is not defined
