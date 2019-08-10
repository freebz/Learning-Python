# from *로 인한 피해를 최소화하기: _X와 __all__

# unders.py
a, _b, c, _d = 1, 2, 3, 4

from unders import *            # _X가 아닌 이름만 적재
a, c
# (1, 3)
_b
# NameError: name '_b' is not defined

import unders                   # 하지만 다른 임포트 주체는 모든 이름을 얻을 수 있음
unders._b
# 2


# alls.py
__all__ = ['a', '_c']           # __all__은 _X에 우선함
a, b, _c, _d = 1, 2, 3, 4

from alls import *              # __all__에 있는 이름만 적재
a, _c
# (1, 3)
b
# NameError: name 'b' is not defined


from alls import a, b, _c, _d   # 하지만 다름 임포트 주체는 모든 이름을 가짐
a, b, _c, _d
# (1, 2, 3, 4)

import alls
alls.a, alls.b, alls._c, alls._d
# (1, 2, 3, 4)
