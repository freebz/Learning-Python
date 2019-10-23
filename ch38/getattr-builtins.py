# -*- coding: utf-8 -*-
class GetAttr:
    eggs = 88                       # eggs: 클래스에 저장, spam: 인스턴스에 저장
    def __init__(self):
        self.spam = 77
    def __len__(self):              # 여기서는 len이 필요함, 그렇지 않으면 __len__에 대해 __getattr__이 호출됨
        print('__len__: 42')
        return 42
    def __getattr__(self, attr):    # __str__ 호출이 아닐 경우 더미 함수
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None

class GetAttribute(object):     # 2.X에서는 object 필요, 3.X에서는 암묵적임
    eggs = 88                   # 2.X에서는 자동으로 모두 isinstance(object)
    def __init__(self):         # __getattribute__, __X__ 기본값을 포함한 새로운 형식의 
        self.spam = 77          # 도구를 사용하려면 반드시 파생되어야 함
    def __len__(self):
        print('__len__: 42')
        return 42
    def __getattribute__(self, attr):
        print('__getattribute__: ' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None

for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))

    X = Class()
    X.eggs                      # 클래스 속성
    X.spam                      # 인스턴스 속성
    X.other                     # 누락한 속성
    len(X)                      # 명시적으로 정의된 __len__

# 새 형식 클래스는 [], +, call 직접 호출을 지원해야 함, 여기서 재정의

    try:    X[0]                # __getitem__?
    except: print('fail []')

    try:    X + 99              # __add__?
    except: print('fail +')

    try:    X()                 # __call__?(내장된 동작을 통한 암묵적 호출)
    except: print('fail ()')

    X.__call__()                # __call__?(명시적, 상속되지 않음)
    print(X.__str__())          # __str__?(명시적, type에서 상속함)
    print(X)                    # __str__?(내장된 동작을 통한 암묵적 호출)
