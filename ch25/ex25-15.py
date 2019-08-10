# 재귀적 리로더

# 재귀적 리로드 테스트하기
c:\Python36\python reloadall.py
reloading reloadall
reloading types

C:\Python27\python reloadall.py
reloading reloadall
reloading types


reloadall.py pybench


from reloadall import reload_all
import os, tkinter
reload_all(os)                  # 일반 사용 모드
# reloading os
# reloading abc
# reloading sys
# reloading errno
# reloading stat
# reloading posixpath
# reloading genericpath

reload_all(tkinter)
# reloading tkinter
# reloading enum
# reloading sys
# reloading _tkinter
# reloading tkinter.constants
# reloading re
# reloading sre_compile
# reloading _sre
# reloading sre_parse
# reloading functools
# reloading _locale
# reloading copyreg


import b                        # a.py 파일
X = 1

import c                        # b.py 파일
Y = 2

Z = 3                           # c.py 파일


# py -3
import a
a.X, a.b.Y, a.b.c.Z
# (1, 2, 3)

# 파이썬을 종료하지 않고 세 파일의 할당 값을 변경하고서 저장

from imp import reload
relaod(a)                       # 내장된 reload는 최상위 레벨에만 적용
# <module 'a' from '.\\a.py'>
a.X, a.b.Y, a.b.c.Z
# (111, 2, 3)

from reloadall import reload_all
reload_all(a)                   # 일반 사용 모드
# reloading a
# reloading b
# relaoding c
a.X, a.b.Y, a.b.c.Z             # 모든 중첩된 모듈로 리로드
# (111, 222, 333)
