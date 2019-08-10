# 재귀적 from 임포트는 동작하지 않을 수도 있음

# recur1.py
X = 1
import recur2                   # 아직 존재하지 않는다면 지금 recur2 실행
Y = 2

# recur2.py
from recur1 import X            # OK: "X"는 이미 할당됨
from recur1 import Y            # 에러: "Y"는 아직 할당되지 않음

# py -3
import recur1
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "./recur1.py", line 3, in <module>
#     import recur2
#   File "./recur2.py", line 3, in <module>
#     from recur1 import Y
# ImportError: cannot import name 'Y'
