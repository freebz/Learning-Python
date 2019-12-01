class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):     # 내장된 동작이 아니라 이름으로
        print('In SuperMeta.call:', classname)
        return type.__call__(meta, classname, supers, classdict)

class SubMeta(SuperMeta):                                 # 타입에 의해 생성됨
    def __init__(Class, classname, supers, classdict):    # type.__init__ 오버라이드
        print('In SubMeta init:', classname)

print(SubMeta.__class__)
print([n.__name__ for n in SubMeta.__mro__])
print()
print(SubMeta.__call__)                     # 이름으로 발견된다면 데이터 디스크립터가 아님
print()
SubMeta.__call__(SubMeta, 'xxx', (), {})    # 명시적 호출은 동작: 클래스 상속
print()
SubMeta('yyy', (), {})                      # 그러나 암묵적 내장된 동작은 동작하지 않음: 타입

