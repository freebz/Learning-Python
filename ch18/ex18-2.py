# 가변 인수 변경 피하기

L = [1,2]
changer(X, L[:])                # 사본을 전달하기 때문에 'L'은 변경되지 않음


def changer(a, b):
    b = b[:]                    # 입력된 리스트를 복사함으로써 호출자에 영향을 주지 않음
    a = 2
    b[0] = 'spam'               # 우리가 만든 사본만 변경함


L = [1, 2]
changer(X, tuple(L))            # 튜플 전달, 변경하려 하면 에러가 발생함
