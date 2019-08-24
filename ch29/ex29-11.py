# 중첩 클래스: LEGB 범위 규칙 다시 살펴보기

X = 1

def nester():
    print(X)                    # 전역 변수: 1
    class C:
        print(X)                # 전역 변수: 1
        def method1(self):
            print(X)            # 전역 변수: 1
        def method2(self):
            X = 3               # 전역 변수 숨김
            print(X)            # 지역 변수: 3
    I = C()
    I.method1()
    I.method2()

print(X)                        # 전역 변수: 1
nester()                        # 나머지: 1, 1, 1, 3
print('-'*40)


X = 1

def nester():
    X = 2                       # 전역 변수 숨김
    print(X)                    # 지역 변수: 2
    class C:
        print(X)                # 둘러싼 함수인 def(nester) 안: 2
        def method1(self):
            print(X)            # 둘러싼 함수인 def(nester) 안: 2
        def method2(self):
            X = 3               # 둘러싼 함수(nester)를 숨김
            print(X)            # 지역 변수: 3
    I = C()
    I.method1()
    I.method2()

print(X)                        # 전역 변수: 1
nester()                        # 나머지 2, 2, 2, 3
print('-'*40)


X = 1

def nester():
    X = 2           # 전역 변수를 숨긴다
    print(X)        # 지역 변수: 2
    class C:
        X = 3       # 클래스 지역 변수가 nester의 지역 변수를 숨긴다: C.X 또는 I.X
        print(X)    # 지역 변수: 3
        def method1(self):
            print(X)            # 둘러싼 def의 지역 변수(클래스의 3이 아니다!): 2
            print(self.X)       # 클래스 지역 변수 상속: 3
        def method2(self):
            X = 4               # 둘러싼 함수를 숨긴다(클래스가 아닌 nester)
            print(X)            # 지역 변수: 4
            self.X = 5          # 클래스를 숨김
            print(self.X)       # 인스턴스 내에 위치한 변수: 5
    I = C()
    I.method1()
    I.method2()

print(X)                        # 젼역 변수: 1
nester()                        # 나머지: 2, 3, 2, 3, 4, 5
print('-'*40)
