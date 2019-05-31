# 더 생각해 볼 주제: open 사용자 정의하기

import builtins
def makeopen(id):
    original = builtins.open
    def custom(*pargs, **kargs):
        print('Custom oepn call %r: ' % id, pargs, kargs)
        return original(*pargs, **kargs)
    builtins.open = custom
