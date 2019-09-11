# 왜 팩토리인가?

classname = ...설정 파일에서 읽어 들임...
classarg  = ...설정 파일에서 읽어 들임...

import streamtypes                          # 수정 가능한 코드
aclass = getattr(streamtypes, classname)    # 모듈로부터 가져옴
reader = factory(aclass, classarg)          # 또는 aclass(classarg)
processor(reader, ...)
