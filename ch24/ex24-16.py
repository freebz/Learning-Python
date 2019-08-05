# 상대 그리고 절대 임포트로 모듈 선택하기

# del string*                   # 3.2+에서의 바이트 코드를 위해 __pycache__\stirng* 삭제

# code\pkg\spam.py
import string                   # <== 2.X에서는 상대, 3.X에서는 절대
print(string)

# code\pkg\string.py
print('Ni' * 8)


# c:\Python36\python
import pkg.spam
# <module 'string' from 'C:\\Python36\\lib\\string.py'>

# c:\Python27\python
import pkg.spam
# NiNiNiNiNiNiNiNi
# <module 'pkg.string' from 'pkg\string.py'>


# code\pkg\spam.py
from . import string            # <== 2.X와 3.X 모두에서 상대 임포트
print(string)

# code\pkg\string.py
print('Ni' * 8)

# c:\Python36\python
import pkg.spam
# NiNiNiNiNiNiNiNi
# <module 'pkg.string' from '.\\pkg\\string.py'>

# c:\Python27\python
import pkg.spam
# NiNiNiNiNiNiNiNi
# <module 'pkg.string' from '\pkg\string.py'>
