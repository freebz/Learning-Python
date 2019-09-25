# 슈퍼클래스의 다중 __slots__ 리스트

class E:
    __slots__ = ['c', 'd']           # 슈퍼클래스는 슬롯을 가짐
class D(E):
    __slots__ = ['a', '__dict__']    # 서브클래스도 슬롯을 가지고 있음

X = D()
X.a = 1; X.b = 2; X.c = 3            # 인스턴스는 union(slots: a, c)
X.a, X.c
# (1, 3)


E.__slots__                     # 하지만 슬롯은 연결되지 않음
# ['c', 'd']
D.__slots__
# ['a', '__dict__']
X.__slots__                     # 인스턴스는 *가장 낮은* __slots__을 상속받음
# ['a', '__dict__']
X.__dict__                      # 그리고 자신만의 속성 딕셔너리도 가지고 있음
# {'b': 2}

for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
    print(attr, '=>', getattr(X, attr))

# b => 2                        # 다른 슈퍼클래스 슬롯은 누락됨!
# a => 1
# __dict__ => {'b': 2}

dir(X)                          # 하지만 dir()는 모든 슬롯 이름을 포함함
# [...다수의 이름이 생략됨... 'a', 'b', 'c', 'd']
