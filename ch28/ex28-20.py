# 인스턴스 vs 클래스 속성

from person import Person       # 2.X: keys는 리스트, dir은 덜 보여 줌
bob = Person('Bob Smith')

bob.__dict__.keys()             # 인스턴스 속성만
# ['name', 'job', 'pay']

dir(bob)                        # 클래스의 상속된 속성까지 보여 줌
# ['__doc__', '__init__', '__module__', '__repr__', 'giveRaise', 'job', 'lastName', 'name', 'pay']


list(bob.__dict__.keys())       # 3.X keys는 뷰 형태로 리스트가 아님
# ['name', 'job', 'pay']

dir(bob)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'giveRaise', 'job', 'lastName', 'name', 'pay']


len(dir(bob))
# 31
list(name for name in dir(bob) if not name.startswith('__'))
# ['giveRaise', 'job', 'lastName', 'name', 'pay']
