# 파이썬 3.X의 print 함수 흉내 내기

from __future__ import print_function


from print3 import print3
print3(1, 2, 3)
print3(1, 2, 3, sep='')         # 구분자를 제거
print3(1, 2, 3, sep='...')
print3(1, [2], (3,), sep='...') # 다양한 객체 타입

print3(4, 5, 6, sep='', end='') # 줄바꿈 제거
print3(7, 8, 9)
print3()                        # 줄바꿈 추가(또는 빈 라인)

import sys
print3(1, 2, 3, sep='??', end='.\n', file=sys.stderr) # 파일로 리다이렉트


# c:\python27\python testprint3.py
# 1 2 3
# 123
# 1...2...3
# 1...[2]...(3,)
# 4567 8 9

# 1??2??3.
