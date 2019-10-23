# __getattribute__ 사용하기

class AttrSquare:                             # 2.X에서는 (object) 추가
    def __init__(self, start):
        self.value = start                    # __setattr__ 호출!

    def __getattribute__(self, attr):         # 모든 속성 가져오기를 캐치
        if attr == 'X':
            return self.value ** 2            # __getattribute__ 다시 호출!
        else:
            return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):       # 모든 속성 할당을 캐치
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)


def __getattribute__(self, attr):
    if attr == 'X':
        return object.__getattribute__(self, 'value') ** 2
