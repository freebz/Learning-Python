# 패키지 임포트 예제

# dir1\__init__.py
print('dir1 init')
x = 1

# dir1\dir2\__init__.py
print('dir2 init')
y = 2

# dir1\dir2\mod.py
print('in mod.py')
z = 3


# python                        # dir1의 컨테이너 디렉터리에서 실행
import dir1.dir2.mod            # 처음 임포트할 때 초기화 파일을 실행함
# dir1 init
# dir2 init
# in mod.py

import dir1.dir2.mod            # 나중에 임포트할 때는 실행하지 않음


from imp import reload          # from은 3.X에서만 필요함
reload(dir1)
# dir1 init
# <module 'dir1' from './dir1/__init__.py'>

reload(dir1.dir2)
# dir2 init
# <module 'dir1.dir2' from './dir1/dir2/__init__.py'>


dir1
# <module 'dir1' from './dir1/__init__.py'>
dir1.dir2
# <module 'dir1.dir2' from './dir1/dir2/__init__.py'>
dir1.dir2.mod
# <module 'dir1.dir2.mod' from './dir1/dir2/mod.py'>


dir1.x
# 1
dir1.dir2.y
# 2
dir1.dir2.mod.z
# 3
