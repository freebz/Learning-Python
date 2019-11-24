# 코드 변형: 라우터, 디스크립터, 자동화

class BuiltinsMixin:
    def reroute(self, attr, *args, **kargs):
        return self.__class__.__getattr__(self, attr)(*args, **kargs)

    def __add__(self, other):
        return self.reroute('__add__', other)
    def __str__(self):
        return self.reroute('__str__')
    def __getitem__(self, index):
        return self.reroute('__getitem__', index)
    def __call__(self, *args, **kargs):
        return self.reroute('__call__', *args, **kargs)
    # 다른 필요한 것들은 여기에 추가


class BuiltinsMixin:
    class ProxyDesc(object):                                    # 2.X에서는 object
        def __init__(self, attrname):
            self.attrname = attrname
        def __get__(self, instance, owner):
            return getattr(instance._wrapped, self.attrname)    # _wrapped로 가정

    builtins = ['add', 'str', 'getitem', 'call']                # 다른 것들도 추가
    for attr in builtins:
        exec('__%s__ = ProxyDesc("__%s__")' % (attr, attr))


        __add__ = ProxyDesc("__add__")
        __str__ = ProxyDesc("__str__")
        ...등등...
