# 혼합(Mix-in) 슈퍼클래스들

class BuiltinsMixin:
    def __add__(self, other):
        return self.__class__.__getattr__(self, '__add__')(other)
    def __str__(self):
        return self.__class__.__getattr__(self, '__str__')()
    def __getitem__(self, index):
        return self.__class__.__getattr__(self, '__getitem__')(index)
    def __call__(self, *args, **kargs):
        return self.__class__.__getattr__(self, '__call__')(*args, **kargs)
    # 다른 필요한 것들은 여기에 추가

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance(BuiltinsMixin):
            ...나머지 부분은 변경 사항 없음...
            def __getattr__(self, attr): ...
            def __setattr__(self, attr, value): ...

class BuiltinsMixin:
    def __add__(self, other):
        return self._wrapped + other    # _wrapper를 가정함
    def __str__(self):                  # __getattr__ 건너뜀
        return str(self._wrapped)
    def __getitme__(self, index):
        return self._wrapped[index]
    def __call__(self, *args, **kargs):
        return self._wrapped(*args, **kargs)
    # 다른 필요한 것들은 여기에 추가

def accessControl(failIf):
    def onInstance(aClass):
        class onInstance(BuiltinsMixin):
            ...그리고 self.__wrapped 대신 self._wrapped 사용...
            def __getattr__(self, attr): ...
            def __setattr__(self, attr, value): ...
