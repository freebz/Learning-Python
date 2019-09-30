# 예외 발생시키기

raise IndexError                # 클래스(생성된 인스턴스)
raise IndexError()              # 인스턴스(문에서 생성됨)


exc = IndexError()              # 인스턴스를 미리 생성
raise exc

excs = [IndexError, TypeError]
raise excs[0]


try:
    ...
except IndexError as X:         # X에는 발생한 인스턴스 객체가 할당됨
    ...


class MyExc(Exception): pass
...
raise MyExc('spam')             # 생성자 인수를 가진 예외 클래스
...
try:
    ...
except MyExc as X:              # 예외 처리기에서 인스턴스 속성을 이용할 수 있음
    print(X.args)
