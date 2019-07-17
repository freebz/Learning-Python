# 초기화 코드

print('hello')
spam = 1                        # 변수 초기화


# python
import simple                   # 첫 import: 파일 코드를 적재하고 실행함
# hello
simple.spam                     # 할당은 속성을 만듦
# 1


simple.spam = 2                 # 모듈에서 속성을 변경
import simple                   # 이미 적재된 모듈을 가져옴
simple.spam                     # 코드가 재실행되지 않음: 속성은 변하지 않음
# 2
