import threenames               # 모듈 전체 로드: 여기서 실행됨

threenames.b, threenames.c      # 몯듈의 속성에 접근

from threenames import a, b, c  # 다수의 이름을 바깥으로 복사


dir(threenames)
