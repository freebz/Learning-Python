# 클래스는 모듈 안의 속성

from modulename import FirstClass    # 이름을 내 범위 안으로 복사
class SecondClass(FirstClass):       # 클래스 이름을 직접 사용
    def display(self): ...


import modulename                            # 전체 모듈에 접근
class SecondClass(modulename.FirstClass):    # 참조하기 위해 한정
    def display(self): ...


# food.py
var = 1                         # food.var
def func(): ...                 # food.func
class spam: ...                 # food.spam
class ham: ...                  # food.ham
class eggs: ...                 # food.eggs


# person.py
class person: ...


import person                   # 모듈 임포트
x = person.person()             # 모듈 안의 클래스


from person import person       # 모듈에서 클래스 가져오기
x = person()                    # 클래스 이름 사용


import person                   # 모듈은 소문자
x = person.Person()             # 클래스는 대문자
