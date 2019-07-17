# 네임스페이스ㅜ 딕셔너리: __dict__

list(module2.__dict__.keys())
# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'sys', 'name', 'func', 'klass']


list(name for name in module2.__dict__.keys() if not name.startswith('__'))
# ['sys', 'name', 'func', 'klass']
list(name for name in module2.__dict__ if not name.startswith('__'))
# ['sys', 'name', 'func', 'klass']


module2.name, module2.__dict__['name']
# (42, 42)
