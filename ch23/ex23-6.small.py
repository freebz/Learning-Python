# import와 from은 할당

# 모듈에서 가변 객체를 변경하기

x = 1
y = [1, 2]


# python
from small import x, y          # 두 개의 이름을 복사
x = 42                          # 지역 x만 변경
y[0] = 42                       # 공유 가변 객체를 제자리에서 변경


import small                    # 모듈 이름 가져오기(from은 가져오지 않음)
small.x                         # small의 x는 공유된 x가 아님
# 1
small.y                         # 하지만 우리는 하나의 변경된 가변 객체를 공유함
# [42, 2]
