# 임의의 인수들

def func(*kargs, **pargs): pass
code = func.__code__
code.co_nlocals, code.co_varnames
# (2, ('kargs', 'pargs'))
code.co_argcount, code.co_varnames[:code.co_argcount]
# (0, ())

def func(a, b, *kargs, **pargs): pass
code = func.__code__
code.co_argcount, code.co_varnames[:code.co_argcount]
# (2, ('a', 'b'))
