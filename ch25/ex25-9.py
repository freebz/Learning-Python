# import와 from에 대한 as 확장

import modulename as name       # modulename이 아니라 name을 사용


import modulename
name = modulename
del modulename                  # 원래 이름을 유지하지 않음


from modulename import attrname as name # attrname이 아니라, name 사용


import reallylongmodulename as name # 더 짧은 별명 사용
name.func()

from module1 import utility as util1 # 단 하나의 'utility'만 가질 수 있음
from module2 import utility as util2
util1(); util2();


import dir1.dir2.mod as mod     # 단 한 번만 전체 경로를 기재하면 됨
mod.func()

from dir1.dir2.mod import func as modfunc # 필요 시. 유일하게 만들기 위해 재명명
modfunc()


import newname as oldname
from library import newname as oldname
...그리고 코드 전체를 업데이트할 시간이 날 때까지 행목하게 oldname을 계속 사용하면 됨...
