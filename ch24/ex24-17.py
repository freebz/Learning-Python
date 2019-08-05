# 상대 임포트는 패키지만 검색

# code\pkg\spam.py
from . import string            # <== 여기에 string.py가 없다면 2.X와 3.X 모두에서 실패!

# del pkg\string*

# c:\Python36\python
import pkg.spam
# ImportError: cannot import name string

# c:\Python27\python
import pkg.spam
# ImportError: cannot import name string
