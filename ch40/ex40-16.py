# 디스크립터 특별 케이스

class C: pass                       # 상속 특별 케이스 #1...
I = C()                             # 클래스 데이터 스크립터는 우선권을 가짐
I.__class__, I.__dict__
# (<class '__main__.C'>, {})

I.__dict__['name'] = 'bob'          # 인스턴스에서의 동적 데이터
I.__dict__['__class__'] = 'spam'    # 속성이 아니라 키를 할당
I.__dict__['__dict__'] = {}

I.name                              # 일반적으로 I.name은 I.__dict__로부터 유래
# 'bob'                             # 하지만 I.__class_와 I.__dict는 그렇지 않음!
I.__class__, I.__dict__
# (<class '__main__.C'>, {'name': 'bob', '__class__': 'spam', '__dict__': {}})


class D:
    def __get__(self, instance, owner): print('__get__')
    def __set__(self, instance, value): print('__set__')

class C: d = D()                # 데이터 디스크립터 속성
I = C()
I.d                             # 상속된 데이터 스크립터에 접근
# __get__
I.d = 1
# __set__
I.__dict__['d'] = 'spam'        # 인스턴스 네임스페이스 딕셔너리에 동일 이름 정의
I.d                             # 하지만 클래스에서 데이터 디스크립터를 숨기지 않음!
# __get__


class D:
    def __get__(self, instance, owner): print('__get__')

class C: d = D()
I = C()
I.d                             # 상속된 데이터 디스크립터가 아닌 디스크립터에 접근
# __get__
I.__dict__['d'] = 'spam'        # 일반 상속 규칙에 따라 클래스의 이름들을 숨김
I.d
# 'spam'
