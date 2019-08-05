# 네임스페이스 패키지의 실제 사례

# mkdir ns\dir1\sub             # 서로 다른 디렉터리에 동일한 이름의 두 개의 디렉터리
# mkdir ns\dir2\sub             # 윈도우 밖에서도 유사함

# type ns\dir1\sub\mod1.py      # 서로 다른 디렉터리의 모듈 파일들
print(r'dir1\sub\mod1')

# type ns\dir2\sub\mod2.py
print(r'dir2\sub\mod2')

# set PYTHONPATH=C:\code\ns\dir1;C:\code\ns\dir2


# C:\Python36\python
import sub
sub                             # 네임스페이스 패키지: 중첩된 검색 경로
# <module 'sub' (namespace)>
sub.__path__
# _NamespacePath(['C:\\code\\ns\\dir1\\sub', 'C:\\code\\ns\\dir2\\sub'])

from sub import mod1
# dir1\sub\mod1
import sub.mod2                 # 두 개의 서로 다른 디렉터리로부터의 내용
# dir2\sub\mod2

mod1
# <module 'sub.mod1' from 'C:\\code\\ns\\dir1\\sub\\mod1.py'>
sub.mod2
# <module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>


# C:\Python36\python
import sub.mod1
# dir1\sub\mod1
import sub.mod2                 # 한 개의 패키지가 두 개의 디렉터리에 걸쳐 존재함
# dir2\sub\mod2

sub.mod1
# <module 'sub.mod1' from 'C:\\code\\ns\\dir1\\sub\\mod1.py'>
sub.mod2
# <module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>

sub
# <module 'sub' (namespace)>
sub.__path__
# _NamespacePath(['C:\\code\\ns\\dir1\\sub', 'C:\\code\\ns\\dir2\\sub'])


# type ns\dir1\sub\mod1.py
from . import mod2              # 그리고 'from . import string'은 여전히 실패
print(r'dir1\sub\mod1')

# C:\Python36\python
import sub.mod1                 # mod2 의 상대 임포트는 다른 디렉터리에서
# dir2\sub\mod2
# dir1\sub\mod1


import sub.mod2                 # 이미 임포트된 모듈은 다시 실행하지 않음
sub.mod2
# <module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>
