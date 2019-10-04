# sys.exc_info 상세

try:
    ...
except:
    # sys.exc_info()[0:2]는 예외 클래스와 인스턴스임


try:
    ...
except General as instance:
    # instance.__class__는 예외 클래스임


try:
    ...
except General as instance:
    # instance.method()는 이 인스턴스를 위해 최적의 일을 함
