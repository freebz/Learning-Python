# def는 런타임에 실행됨

if test:
    def func():                 # 함수를 이렇게 정의하거나
        ...
else:
    def func():                 # 아니면 이렇게 정의함
        ...
...
func()                          # 선택되어 빌드된 버전을 호출


othername = func                # 함수 객체 할당
othername()                     # 다시 함수를 호출


def func(): ...                 # 함수 객체 생성
func()                          # 객체 호출
func.attr = value               # 속성 추가
