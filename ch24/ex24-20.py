# 이슈

# code\pkg\main.py
import spam

# code\pkg\spam.py
import eggs                     # <= '.' = 메인스크립트의 홈 디렉터리라면 동작함

# code\pkg\eggs.py
print('Eggs' * 4)               # 하지만 3.X에서 패키지로 사용된다면 이 파일은 적재되지 않음!

# python pkg\main.py            # 2.X와 3.X에서 프로그램으로는 OK
EggsEggsEggsEggs

# python pkg\spam.py
EggsEggsEggsEggs

py -2                           # 2.X에서 패키지로는 OK: 상대적이었다 그 후에는 절대적인
import pkg.spam                 # 2.X: 평이한 임포트는 패키지 디렉터리를 먼저 검색함
EggsEggsEggsEggs

py -3                           # 하지만 3.X는 파일을 찾는 데 실패: 절대 임포트만 사용
import pkg.spam                 # 3.X: 평이한 임포트는 CWD와 sys.path만 검색함
# ImportError: No module named 'eggs'


# code\pkg\main.py
import spam

# code\pkg\spam.py
from . import eggs              # <== 메인 파일이 여기에 있다면 패키지가 아님(그것이 나라도)!

# code\pkg\eggs.py
print('Eggs' * 4)

# python                        # 3.X와 2.X 모두에서 패키지로는 OK, 프로그램으로는 NO
import pkg.spam
EggsEggsEggsEggs

# python pkg\main.py
# SystemError: ... cannot perform relative import
# python pkg\spam.py
# SystemError: ... cannot perform relative import
