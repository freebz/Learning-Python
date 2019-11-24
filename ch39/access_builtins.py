"""
파일 access_builtins.py(from access2_builtins2b.py)
일부 내장 연산을 프록시 클래스의 __getattr__에 전달하여,
3.X에서도 직접적인 이름 호출과 2.X의 기본 고전 클래스처럼 동일하게 동작하도록 함
이를 요구대로 프록시된 객체가 사용하는 다른 __X__이름들을 포함하도록 확장해 보자
"""

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

    # 3.X에서만 래퍼 객체에 의해 사용되는 다른 내용들 추가
