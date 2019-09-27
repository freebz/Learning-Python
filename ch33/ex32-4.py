# 사용자 정의 예외

class AlreadyGotOne(Exception): pass    # 사용자 저의 예외

def grail():
    raise AlreadyGotOne()               # 인스턴스가 발생함

try:
    grail()
except AlreadyGotOne:                   # 클래스 이름을 캐치
    print('got excpetion')

# got excpetion


class Career(Exception):
    def __str__(self): return 'So I became w waiter...'

raise Career()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.Career: So I became w waiter...
