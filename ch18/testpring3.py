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
