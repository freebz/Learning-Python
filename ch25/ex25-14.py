# 예제: 이행적 모듈 리로드

# A.py
import B                        # A가 리로드될 때, B와 C는 리로드되지 않음!
import C                        # 이미 적재된 모듈을 임포트하기만 함: 아무 동작도 하지 않음

# python
from imp import reload
relaod(A)
