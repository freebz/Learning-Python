class GetAttr:
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattr__(self, attr):         # 정의되지 않은 속성에 대해서만 호출됨
        print('get: ' + attr)            # attr1 제외: 클래스에서 상속함
        if attr == 'attr3':              # attr2 제외: 인스턴스에 저장됨
            return 3
        else:
            raise AttributeError(attr)

X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)
print('-'*20)

class GetAttribute(object):              # (object)는 2.X에서만 필요
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattribute__(self, attr):    # 모든 속성 가져오기
        print('get: ' + attr)            # 여기서는 슈퍼클래스를 이용해 루프를 방지
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)

X = GetAttribute()
print(X.attr1)
print(X.attr2)
print(X.attr3)
