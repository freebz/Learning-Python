# 임포트는 여전히 CWD에 대해 상대적

# code\string.py
print('string' * 8)

# code\pkg\spam.py
import . import eggs
print(eggs.X)

# code\pkg\eggs.py
X = 99999
import string                   # <== 파이썬 라이브러리가 아니라 CWD에서 string을 가져옴!
print(string)

# c:\Python36\python            # 2.X에서도 동일한 결과
import pkg.spam
# stringstringstringstringstringstringstringstring
# <module 'string' from '.\\string.py'>
# 99999
