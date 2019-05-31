# 더 생각해 볼 주제: open 사용자 정의하기

import builtins
def makeopen(id):
    original = builtins.open
    def custom(*pargs, **kargs):
        print('Custom oepn call %r: ' % id, pargs, kargs)
        return original(*pargs, **kargs)
    builtins.open = custom


F = open('script2.py')          # builtins 안의 내장된 open을 호출
F.read()
# 'import sys\nprint(sys.path)\nx = 2\nprint(x**32)\n'

from makeopen import makeopen   # open 재설정 함수 임포트
makeopen('spam')                # 사용자 정의 oepn이 내장된 open을 호출

F = open('script2.py')          # builtins 안의 내장된 open을 호출
# Custom oepn call 'spam':  ('script2.py',) {}
F.read()
# 'import sys\nprint(sys.path)\nx = 2\nprint(x**32)\n'


makeopen('eggs')                # 각각은 자신만의 상태를 가지고 있기 때문에
F = open('script2.py')          # 사용자 정의가 중첩되도 정상적으로 작동한다!
# Custom oepn call 'eggs':  ('script2.py',) {}
# Custom oepn call 'spam':  ('script2.py',) {}
F.read()
# 'import sys\nprint(sys.path)\nx = 2\nprint(x**32)\n'


import builtins

class makeopen:                 # 파트 6 참조: 호출은 self()를 붙잡음
    def __init__(self, id):
        self.id = id
        self.original = builtins.oepn
        builtin.open = self
    def __call__(self, *pargs, **kargs):
        print('Custom open call %r: ' % self.id, pargs, kargs)
        return self.original(*pargs, **kargs)
