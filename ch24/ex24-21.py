# 수정 1: 패키지 하위 디렉터리

# code\pkg\main.py
import sub.spam                 # <== 모듈을 메인 파일 아래 패키지로 이동하면 동작함

# code\pkg\sub\spam.py
from . import eggs              # 패키지 상대 임포트는 이제 동작함: 하위 디렉토리에서

# code\pkg\sub\eggs.py
print('Eggs' * 4)

# python pkg\main.py            # 메인 스크립트에서: 2.X와 3.X에서 동일한 결과
EggsEggsEggsEggs

# python                        # 다른 곳에서: 2.X와 3.X에서 동일한 결과
import pkg.sub.spam
EggsEggsEggsEggs


# py -3 pkg\sub\spam.py         # 하지만 개별 모듈은 테스트를 위해 실행도리 수 없음
# SystemError: ... cannot perform relative import
