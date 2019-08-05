# 3.X에서 상대적인 임포트 해결 방법

import string                   # string을 패키지 외부에서 임포트함(절대 경로)


from string import name         # name을 패키지 외부의 string으로부터 임포트함


from . import string            # 여기서는 mypkg.string을 임포트(상대 경로)


from .string import name1, name2 # mypkg.string으로부터 이름들을 임포트


from .. import spam             # mypkg의 형제들을 임포트함


from . import D                 # A.B.D를 임포트(.은 A.B를 의미)
from .. import E                # A.E를 임포트(..은 A를 의미)

from .D import X                # A.B.D.X를 임포트(.은 A.B를 의미)
from ..E import X               # A.E.X를 임포트(..은 A를 의미)
