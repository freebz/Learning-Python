# 메타클래스 메서드 vs 클래스 메서드

class A(type):
    def a(cls):                         # 메타클래스 메서드: gets class
        cls.x = cls.y + cls.z

class B(metaclass=A):
    y, z = 11, 22
    @classmethod                        # 클래스 메서드: gets class
    def b(cls):
        return cls.x

B.a()                        # 메타클래스 메서드 호출, 클래스에서만 볼 수 있음
B.x                          # B에 클래스 데이터를 생성, 일반 인스턴스에서도 접근 가능
# 33

I = B()
I.x, I.y, I.z
# (33, 11, 22)

I.b()                        # 클래스 메서드: 인스턴스가 아니라 클래스를 보냄, 인스턴스에 보임
# 33
I.a()                        # 메타클래스 메서드: 클래스를 통해서만 접근 가능
# AttributeError: 'B' object has no attribute 'a'
