# 클래스 인터페이스 기법

class Super:
    def method(self):
        print('in Super.method')             # 기본 동작
    def delegate(self):
        self.action()                        # 서브클래스에서 정의해야 함

class Inheritor(Super):                      # 메서드를 그대로 상속
    pass

class Replacer(Super):                       # 메서드를 완전히 대체함
    def method(self):
        print('in Replacer.method')

class Extender(Super):                       # 메서드의 동작을 확장
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):                       # 필요한 메서드를 채워 넣음
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()


# python specialize.py

# Inheritor...
# in Super.method

# Replacer...
# in Replacer.method

# Extender...
# starting Extender.method
# in Super.method
# ending Extender.method

# Provider...
# in Provider.action
