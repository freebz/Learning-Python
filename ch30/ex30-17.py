# 속성 할당과 제거

class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10    # self.name=val이나 setattr가 아니라
        else:
            raise AttributeError(attr + ' not allowed')

X = Accesscontrol()
X.age = 40                                      # __setattr__ 호출
X.age
# 50
X.name = 'Bob'
# ...생략...
# AttributeError: name not allowed


self.age = value + 10              # 루프
setattr(self, attr, value + 10)    # 루프(attr는 'age')


self.other = 99                    # 재귀적이나, 루프가 되지는 않음: 실패


self.__dict__[attr] = value + 10              # OK: 루프가 생기지 않음
object.__setattr__(self, attr, value + 10)    # OK: 루프 X(새로운 형식에서만)
