# 메타클래스 메서드에서의 연산자 오버로딩

class A(type):
    def __getitem__(cls, i):    # 클래스를 처리하기 위한 메타클래스 메서드
        return cls.data[i]      # 내장된 연산은 클래스를 생략하고 메타클래스 메서드 사용
                                # 명시적 이름 검색 클래스 + 메타클래스
class B(metaclass=A):           # 메타클래스에서의 데이터 디스크립터를 먼저 사용
    data = 'spam'

B[0]                            # 메타클래스 인스턴스 이름: 클래스에서만 보임
# 's'
B.__getitem__
# <bound method A.__getitem__ of <class '__main__.B'>>

I = B()
I.data, B.data                  # 일반 상속 이름: 인스턴스와 클래스에서 보임
# ('spam', 'spam')
I[0]
# TypeError: 'B' object does not support indexing


class A(type):
    def __getattr__(cls, name):           # 클래스 B의 getitem에 의해 얻음
        return getattr(cls.data, name)    # 그러나 내장된 기능에 의해 동일하게 동작 x

class B(metaclass=A):
    data = 'spam'

B.upper()
# 'SPAM'
B.upper
# <built-in method upper of str object at 0x7f85a6d04110>
B.__getattr__
# <bound method A.__getattr__ of <class '__main__.B'>>

I = B()
I.upper
# AttributeError: 'B' object has no attribute 'upper'
I.__getattr__
# AttributeError: 'B' object has no attribute '__getattr__'


B.data = [1, 2, 3]
B.append(4)                  # 명시적인 일반 이름들은 메타클래스의 getattr로 라우팅됨
B.data
# [1, 2, 3, 4]
B.__getitem__(0)             # 명시적인 특별한 이름들은 메타클래스의 getattr에 라우팅
# 1
B[0]                         # 하지만 내장된 기능은 메타클래스의 getattr도 생략함?!
# TypeError: 'A' object does not support indexing
