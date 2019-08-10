# 직접 호출: 두 가지 방식

modname = 'string'
string = __import__(modname)
string
# <module 'string' from '/usr/lib/python3.6/string.py'>


import importlib
modname = 'string'
string = importlib.import_module(modname)
string
# <module 'string' from '/usr/lib/python3.6/string.py'>
