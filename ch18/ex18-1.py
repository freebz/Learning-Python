# 인수와 공유 참조

def f(a):                       # a는 전달된 객체에 대한 참조를 할당
    a = 99                      # 지역 변수 a만 변경

b = 88
f(b)                            # 처음에는 a와 b 모두 똑같은 88 참조
print(b)                        # b는 변경되지 않음
# 88


def changer(a, b):              # 인수에는 객체의 참조가 할당됨
    a = 2                       # 지역 이름의 값만 변경
    b[0] = 'spam'               # 공유 객체를 직접 변경

X = 1
L = [1, 2]                      # 호출자:
changer(X, L)                   # 불변 객체와 가변 객체 전달
X, L                            # X는 변경되지 않았지만, L은 변경됨!
# (1, ['spam', 2])


X = 1
a = X                           # 둘은 동일 객체를 공유
a = 2                           # 'a'만 재설정. 'X'는 여전히 1
print(X)
# 1


L = [1, 2]
b = L                           # 둘은 동일 객체를 공유
b[0] = 'spam'                   # 직접 변경. 'L'도 함께 변경됨
print(L)
# ['spam', 2]