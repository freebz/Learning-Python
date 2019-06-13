# 함수 내부 접근

def func(a):
    b = 'spam'
    return b * a

func(8)
# 'spamspamspamspamspamspamspamspam'


func.__name__
# 'func'
dir(func)
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__',
#  ...생략: 총 34개...
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


func.__code__
# <code object func at 0x7f8838abd390, file "/home/fx/work/Learning Python/ch19/ex19-8.py", line 3>

dir(func.__code__)
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# ...생략: 총 37개...
#  'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']

func.__code__.co_varnames
# ('a', 'b')
func.__code__.co_argcount
# 1
