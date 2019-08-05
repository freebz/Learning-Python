# 패키지 상대 임포트의 위험 요소: 복합 용도

from . import mod               # 2.X와 3.X에서 패키지가 아닌 모드에서는 허용되지 않음
import mod                      # 3.X의 패키지 모드에서 파일 자신의 디렉터리를 검색하지 않음


from system.section.mypkg import mod    # 프로그램, 패키지 모드 모두에서 동작함
