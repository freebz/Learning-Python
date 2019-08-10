# 리로드는 from 임포트에 영향을 주지 않을 수도 있음

from module import X            # X는 다름 모듈 리로드에 영향받지 않음!

from imp import reload
reload(module)                  # module은 변경하지만, 내 이름들은 변경하지 않음
X                               # 여전히 예전 객체를 참조


import module                   # 이름이 아니라. 모듈을 가져옴

from imp import reload
reload(module)                  # 모듈을 제자리에서 변경
module.X                        # 현재 X를 가져옴: 모듈 리로드 내용 반영
