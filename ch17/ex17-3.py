# 내장 범위

import builtins
dir(builtins)
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
# 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
# ...생략...
# 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed',
# 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum',
# 'super', 'tuple', 'type', 'vars', 'zip']


zip                             # 일반적인 방법
# <class 'zip'>

import builtins                 # 사용자 정의가 필요한 경우를 위한 방법
builtins.zip
# <class 'zip'>

zip is builtins.zip             # 같은 객체. 서로 다른 검색 방식
# True
