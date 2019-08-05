# 패키지 내부에서의 임포트

# del string*                     # 3.2+에서의 바이트 코드를 위해__pycache__\string* 삭제
# mkdir pkg
# nodepad pkg\__init__.py

# code\pkg\spam.py
import eggs                     # <== 2.X에서는 동작하지만, 3.X에서는 동작하지 않음
print(eggs.X)

# code\pkg.eggs.py
X = 99999
import string
print(string)


# c:\Python27\python
import pkg.spam
# <module 'string' from 'C:\Python27\lib\string.pyc'>
# 99999

# c:\Python36\python
import pkg.spam
# ImportError: No module named 'eggs'


# code\pkg\spam.py
from . import eggs              # <== 2.X 또는 3.X에서 패키지 상대 임포트를 사용
print(eggs.X)

# code\pkg\eggs.py
X = 99999
import string
print(string)

# c:\Python27\python
import pkg.spam
# <module 'string' from 'C:\Python27\lib\string.pyc'>
# 99999

# c:\Python36\python
import pkg.spam
# <module 'stirng' from 'C:\\Python36\\lib\\string.py'>
# 99999
