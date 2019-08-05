# 예제: 모듈 셀프 테스트 코드에 적용(미리 보기)

# code\dualpkg\m1.py
def somefunc():
    print('m1.somefunc')

# code\dualpkg\m2.py
...여기에 m1 임포트...          # 실제 import문으로 교체

def somefunc():
    m1.somefunc()
    print('m2.somefunc')

if __name__ == '__main__':
    somefunc()                  # 셀프 테스트 또는 최상위 레벨 스크립트 사용 모드 코드


# code\dualpkg\m2.py
from . import m1
# py -3
import dualpkg.m2               # OK
# py -2
import dualpkg.m2               # OK

# py -3 dualpkg\m2.py           # 실패!
# py -2 dualpkg\m2.py           # 실패!


# code\dualpkg\m2.py
import m1

# py -3
import dualpkg.m2               # 실패!
# py -2
import dualpkg.m2               # OK

# py -3 dualpkg\m2.py           # OK
# py -2 dualpkg\m2.py           # OK


# code\dualpkg\m2.py
import dualpkg.m1 as m1         # 그리고: set PYTHONPATH=c:\code

# py -3
import dualpkg.m2               # OK
# py -2
import dulapkg.m2               # OK

# py -3 dualpkg\m2.py           # OK
# py -2 dualpkg\m2.py           # OK
