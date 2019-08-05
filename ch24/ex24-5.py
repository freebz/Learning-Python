# 패키지와 사용할 때 from vs import

dir2.mod
# NameError: name 'dir2' is not defined
mod.z
# NameError: name 'mod' is not defined


# python
from dir1.dir2 import mod       # 여기에서만 경로를 코딩하면 됨
# dir1 init
# dir2 init
# in mod.py
mod.z                           # 경로를 반복하지 않음
# 3
from dir1.dir2.mod import z
z
# 3
import dir1.dir2.mod as mod     # 더 짧은 명칭을 사용(25장 참조)
mod.z
# 3
from dir1.dir2.mod import z as modz # 이름 충돌 시, 상동(25장 참조)
modz
# 3
