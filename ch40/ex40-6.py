# 2.X에서의 선언

class Spam(object):                     # 2.X 버전도 object는 선택적?
    __metaclass__ = Meta

class Spam(Eggs, object):               # 일반 슈퍼클래스는 OK: object 추천
    __metaclass__ = Meta
