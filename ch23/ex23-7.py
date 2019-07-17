# 파일 간 이름 변경

# python
from small import x, y          # 두 이름을 복사
x = 42                          # 내 x만 변경

import small                    # 모듈 이름을 가져옴
small.x = 42                    # 다른 모듈의 x를 변경
