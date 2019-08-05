# 임포트는 여전히 CWD에 상대적

# code\string.py
print('string' * 8)

# code\pkg\spam.py
from . import string            # <== 2.X와 3.X 모두에서 상대적
print(string)

# code\pkg\string.py
print('Ni' * 8)


# c:\Python36\python            # 2.X에서도 동일한 결과
import pkg.spam
# NiNiNiNiNiNiNiNi
# <module 'pkg.string' from '.\\pkg\\string.py'>


# code\string.py
print('string' * 8)

# code\pkg\spam.py
import string                   # <== 2.X에서는 상대, 3.X에서는 '절대': CWD!
print(string)

# code\pkg\string
print('Ni' * 8)

# c:\Python36\python
# stringstringstringstringstringstringstringstring
# <module 'string' from '.\\string.py'>

# c:\Python27\python
import pkg.spam
# NiNiNiNiNiNiNiNi
# <module 'pkg.string' from 'pkg\string.pyc'>
