# 상대 임포트 vs 절대 패키지 경로

from mypkg import string        # mypkg.string을 임포트(절대 경로)


from system.section.mypkg import string # 시스템 컨테이너는 sys.path상에만


from . import string            # 상대 임포트 구문
