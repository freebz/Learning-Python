# 추상 슈퍼클래스

class Super:
    def delegate(self):
        self.action()
    def action(self):
        assert False, 'action must be defined!'    # 이 버전이 호출되면 오류 발생

X = Super()
X.delegate()
# AssertionError: action must be defined!


class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('action must be defined!')

X = Super()
X.delegate()
# NotImplementedError: action must be defined!


class Sub(Super): pass

X = Sub()
X.delegate()
# NotImplementedError: action must be defined!

class Sub(Super):
    def action(self): print('spam')

X = Sub()
X.delegate()
# spam
