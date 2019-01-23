# 객체는 가비지 컬렉터(Garbage Collector)에 의해 수집됨

a = 3
a = 'spam'


x = 42
x = 'shrubbery'                 # 42 반환(어디서도 참조하지 않을 경우)
x = 3.1415                      # 'shrubbery' 반환
x = [1, 2, 3]                   # 3.1415 반환
