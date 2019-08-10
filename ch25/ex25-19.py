# from *은 변수의 의미를 모호하게 할 수 있음

from module1 import *           # 나쁨: 내 이름을 조용히 덮어쓸지도..
from module2 import *           # 설상가상: 우리가 무엇을 가진 건지 알 수가 없다!
from module3 import *

func()                          # 음???
