# 클래스 주의 사항

# 클래스 속성 변경의 부작용

class X:
    a = 1                       # 클래스 속성

I = X()
I.a                             # 인스턴스에 의해 상속됨
# 1
X.a
# 1


X.a = 2                         # X보다 많은 것을 변경하게 됨
I.a                             # I도 변경됨
# 2
J = X()                         # J는 X의 런타임에 할당된 값을 상속받음
J.a                             # (하지만 J.a에 할당하는 것은 X또는 I가 아닌 J의 a를 변경)
# 2


class X: pass                         # 속성 네임스페이스를 만듦
class Y: pass

X.a = 1                               # 클래스 속성을 변수로 사용
X.b = 2                               # 어디에서도 인스턴스가 발견되지 않음
X.c = 3
Y.a = X.a + X.b + X.c

for X.i in range(Y.a): print(X.i)     # 0부터 5까지 프린트


class Record: pass
X = Record()
X.name = 'bob'
X.job = 'Pizza maker'
