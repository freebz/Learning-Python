# 네임스페이스 패키지 중첩

# midkr ns\dir2\sub\lower       # 더 중첩된 구성 항목
# type ns\dir2\sub\lower\mod3.py
print(r'dir2\sub\lower\mod3')

# C:\Python36\python
import sub.lower.mod3           # 네임스페이스 패키지에 중첩된 네임스페이스 패키지
# dir2\sub\lower\mod3

# C:\Python36\python
import sub                      # 한 단계씩 더 깊이 접근하면 동일한 결과
import sub.mod2
# dir2\sub\mod2
import sub.lower.mod3
# dir2\lower\mod3

sub.lower                       # 단일 디렉터리 네임스페이스 패키지
# <module 'sub.lower' (namespace)>
sub.lower.__path__
# _NamespacePath(['C:\code\\ns\\dir2\\sub\\lower'])


# mkdir ns\dir1\sub\pkg
# type ns\dir1\sub\pkg\__init__.py
print(r'dir1\sub\pkg\__init__.py')

# C:\Python36\python
import sub.mod2                 # 중첩된 모듈
# dir2\sub\mod2
import sub.pkg                  # 중첩된 일반 패키지
# dir1\sub\pkg\__init__.py
import sub.lower.mod3           # 중첩된 네임스페이스 패키지
# dir2\sub\lower\mod3

sub                             # 모듈. 패키지. 네임스페이스 패키지
# <module 'sub' (namespace)>
sub.mod2
# <module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>
sub.pkg
# <module 'sub.pkg' from 'C:\\code\\ns\\dir1\\sub\\pkg\\__init__.py'>
sub.lower
# <module 'sub.lower' (namespace)>
sub.lower.mod3
# <module 'sub.lower.mod3' from 'C:\\code\\ns\\dir2\\sub\\lower\\mod3.py'>
