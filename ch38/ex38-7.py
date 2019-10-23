# 디스크립터

# 디스크립터 기초

class Descriptor:
    "docstring goes here"
    def __get__(self, instance, owner): ...    # 속성값을 반환한다
    def __set__(self, instance, value): ...    # 반환값이 없다(None)
    def __delete__(self, instance): ...        # 반환값이 없다(None)
