#!python
#-*- coding:utf-8 -*-
"""
mydir.py: 다른 모듈의 네임스페이스를 나열하는 모듈
"""
from __future__ import print_function # 2.X 호환

seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__, 'file:', module.__file__)
        print(sepline)

    count = 0
    for attr in sorted(module.__dict__): # 네임스페이스 키를 스캔(또는 열거)
        print('%02d) %s' % (count, attr), end = ' ')
        if attr.startswith('__'):
            print('<built-in name>') # __file__ 등은 건너뜀
        else:
            print(getattr(module, attr)) # __dict__[attr]와 동일
        count += 1

    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)
        print(sepline)

if __name__ == '__main__':
    import mydir
    listing(mydir)              # 셀프 테스트 코드: 나 자신을 열거
