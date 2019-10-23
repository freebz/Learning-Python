# 읽기 전용 디스크립터

class D:
    def __get__(*args): print('get')

class C:
    a = D()                     # 속성이 디스크립터 인스턴스

X = C()
X.a                             # 상속된 디스크립터의 __get__을 실행
# get
C.a
# get
X.a = 99                        # X에 저장되면 C.a를 숨김!
X.a
# 99
list(X.__dict__.keys())
# ['a']
Y = C()
Y.a                             # Y는 여전히 디스크립터를 상속
# get
C.a
# get


class D:
    def __get__(*args): print('get')
    def __set__(*args): raise AttributeError('cannot set')

class C:
    a = D()

X = C()
X.a                             # C.a__get__으로 라우팅됨
# get
X.a = 99                        # C.a__get__으로 라우팅됨
# AttributeError: cannot set
