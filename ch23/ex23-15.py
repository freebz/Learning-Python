# 모듈 리로드하기

message = "First version"
def printer():
    print(message)


# python
import changer
changer.printer()
# First version


message = "After editing"
def printer():
    print('reloaded:', message)


import changer
changer.printer()               # 아무 효과가 없음: 이미 적재된 모듈 사용
# First version
from imp import reload
reload(changer)                 # 새로운 코드를 적재하해릿 공하도록 강제
# <module 'changer' from '.\\changer.py'>
changer.printer()               # 이제 새로운 버전이 동작함
# reloaded: After editing
