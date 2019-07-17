# import와 from은 같음

from module import name1, name2 # 이 두 개의 이름(만)을 복사하라


import module                   # 모듈 객체를 가져옴
name1 = module.name1            # 할당으로 이름을 복사함
name2 = module.name2
del module                      # 모듈 이름을 삭제함
