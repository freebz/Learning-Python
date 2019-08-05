# 패키지에 상대적인 임포트

# 상대 임포트의 기초

from . import spam              # 이 패키지에 상대적임


from .spam import name


from __future__ import absolute_import # 2.X에서 3.X의 절대 임포트 모델 사용


import string                   # 이 패키지의 버전은 건너뛸 것


from . import string            # 이 패키지에서만 검색할 것


from .string import name1, name2 # mypkg.string으로부터 이름들을 임포트
from . import string             # mypkg.string을 임포트
from .. import string            # mypkg와 같은 디렉터리에 속한 string 모듈을 임포트
