# 왜 예외 계층 구조인가?

try:
    func()
except (General, Specific1, Specific2):    # 이들 중 아무거나 잡아낼 것
    ...


# mathlib.py

class Divzero(Exception): pass
class Oflow(Exception): pass

def func():
    ...
    raise Divzero()

...기타 동작...


# client.py

import mathlib

try:
    mathlib.func(...)
except (mathlib.Divzero, mathlib.Oflow):
    ...처리 및 복구...


# mathlib.py

class Divzero(Exception): pass
class Oflow(Exception): pass
class Uflow(Exception): pass


# client.py

try:
    mathlib.func(...)
except (mathlib.Divzero, mathlib.Oflow, mathlib.Uflow):
    ...처리 및 복구...


# client.py

try:
    mathlib.func(...)
except:                         # 여기에서 모든 것을 다 잡아냄(또는 Exception 슈퍼클래스를 잡음)
    ...처리 및 복구...


# mathlib.py

class NumErr(Exception): pass
class Divzero(NumErr): pass
class Oflow(NumErr): pass

def func():
    ...
    raise DivZero()

...기타 동작...


# client.py

import mathlib

try:
    mathlib.func(...)
except mathlib.NumErr:
    ...전달 및 복구...


# mathlib.py

...
class Uflow(NumErr): pass
