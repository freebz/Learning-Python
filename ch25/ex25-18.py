# from문은 이름을 복사하지, 링크를 복사하지 않음

# nested1.py
X = 99
def printer(): print(X)


# nested2.py
from nexted1 import X, printer  # 이름을 복사
X = 88                          # 내 "X"만 변경!
printer()                       # nested1의 X는 여전히 99

# python nested2.py
# 99


# nested3.py
import nested1                  # 모듈을 전체로 가져옴
nexted1.X = 88                  # OK: nested1의 X를 변경
nested1.printer()

# python nested3.py
# 88
