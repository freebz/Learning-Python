# 함수 속성

func
# <function func at 0x7f8838a7dc80>
func.count = 0
func.count += 1
func.count
# 1
func.handles = 'Button-Press'
func.handles
# 'Button-Press'
dir(func)
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__',
#  ...생략: 3.X에서 다른 이름들은 두 개의 언더스코어 문자가 붙기 때문에 여러분의 이름은 충돌을 피할 수 있다...
#  '__str__', '__subclasshook__', 'count', 'handles']


# py -3
def f(): pass

dir(f)
# ...자세한 내용은 직접 실행하여 확인해 보자...
len(dir(f))
# 34
[x for x in dir(f) if not x.startswith('__')]
# []

# py -2
def f(): pass

dir(f)
# ...자세한 내용은 직접 실행하여 확인해 보자...
len(dir(f))
# 31
[x for x in dir(f) if not x.startswith('__')]
# ['func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc',
#  'func_globals', 'func_name']
