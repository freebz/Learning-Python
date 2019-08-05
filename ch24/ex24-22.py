# 수정 2: 전체 경로 절대 임포트

# code\pkg\main.py
import spam

# code\pkg\spam.py
import pkg.eggs                 # <== 전체 패키지 경로는 모든 경우에 동작함. 2.X+3.X

# code\pkg\eggs.py
print('Eggs' * 4)

# set PYTHONPATH=c:\code
# python pgk\main.py            # 메인 스크립트에서: 2.X와 3.X에서 동일한 결과
EggsEggsEggsEggs

# python                        # 다른 곳에서: 2.X와 3.X에서 동일한 결과
import pkg.spam
EggsEggsEggsEggs


# python pkg\spam.py            # 또한 2.X와 3.X에서 개별 모듈을 실행 가능함
EggsEggsEggsEggs
