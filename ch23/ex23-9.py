# import가 필요한 경우

# M.py
def func():
    ...무엇인가를 수행함...


# N.py
def func():
    ...다른 무엇인가를 수행함...


# O.py
from M import func
from N import func              # M으로부터 가져온 func를 덮어씀
func()                          # N.func만 호출함


# O.py
import M, N                     # 모듈의 이름들이 아니라, 전체 모듈을 가져옴
M.func()                        # 이제 두 이름 모두 호출할 수 있음
N.func()                        # 모듈 이름이 두 이름을 유일하게 만들어줌


# O.py
from M import func as mfunc     # "as"를 이용하여 이름을 유일하게 재명명
from N import func as nfunc
mfunc(), nfunc();               # 하나 또는 나머지의 하나를 호출함
