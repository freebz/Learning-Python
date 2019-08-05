# 패키지 외부에서의 임포트

# c:\Python36\python
import string
string
# <module 'string' from '/usr/lib/python3.6/string.py'>


# code\string.py
print('string' * 8)

# c:\Python36\python
import string
# stringstringstringstringstringstringstringstring

string
# <module 'string' from './string.py'>


from . import string
# SystemError: Parent module '' not loaded, cannot perform relative import


# code\main.py
import string                   # 동일 코드이지만 파일로 작성
print(string)

# C:\Python36\python main.py    # 2.X에서도 동일한 결과
# stringstringstringstringstringstringstringstring
# <module 'string' from 'c:\\code\\string.py'>
