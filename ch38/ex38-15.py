# 속성 가로채기 메서드에서 루프 회피하기

def __getattribute__(self, name):
    x = self.other              # 루프 발생!


def __getattribute__(self, name):
    x = object.__getattribute__(self, 'other')    # 강제로 슈퍼클래스를 통함


def __setattr__(self, name, value):
    self.other = value          # 재귀(아마도 루프가 발생할 것!)


def __setattr__(self, name, value):
    self.__dict__['other'] = value    # 속성 딕셔너리를 이용해 루프 방지


def __setattr__(self, name, value):
    object.__setattr__(self, 'other', value)    # 슈퍼클래스를 이용해 루프 회피


def __getattribute__(self, name):
    x = self.__dict__['other']    # 루프 발생!
