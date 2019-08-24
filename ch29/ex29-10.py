# 네임스페이스의 'Zen': 할당이 이름을 분류

# manynames.py 파일

X = 11                          # 전역(module) 이름/속성(X 또는 manynames.X)

def f():
    print(X)                    # 전역 X에 접근(11)

def g():
    X = 22                      # 지역(함수) 변수(X. 모듈의 X를 숨김)
    print(X)

class C:
    X = 33                      # 클래스 속성(C.X)
    def m(self):
        X = 44                  # 메서드 안의 지역 변수(X)
        self.X = 55             # 인스턴스 속성(instance.X)


# manynames.py(앞에서 계속됨)

if __name__ == '__main__':
    print(X)                    # 11: 모듈(파일 외부에서는 manynames.X로 접근)
    f()                         # 11: 전역
    g()                         # 22: 지역
    print(X)                    # 11: 모듈 이름은 변하지 않음

    obj = C()                   # 인스턴스 생성
    print(obj.X)                # 33: 인스턴스가 상속하는 클래스 이름

    obj.m()                     # 속성 이름X를 인스턴스에 포함시킴
    print(obj.X)                # 55: 인스턴스
    print(C.X)                  # 33: 클래스(인스턴스에 X가 없다면 obj.X로 접근)

    #print(C.m.X)               # 실패: 메서드 안에서만 접근 가능
    #print(g.X)                 # 실패: 함수 안에서만 접근 가능


# otherfile.py

import manynames

X = 66
print(X)                        # 66: 여기까지는 지역 변수
print(manynames.X)              # 11: 임포트 이후 X는 속성이 됨

manynames.f()                   # 11: manynames의 X
manynames.g()                   # 22: 다른 파일의 함수에 있는 지역 변수
print(manynames.C.X)            # 33: 다른 모듈 내의 클래스 속성임
I = manynames.C()
print(I.X)                      # 33: 여기까지는 아직 클래스의 속성임
I.m()
print(I.X)                      # 55: 이제 인스턴스의 속성임


X = 11                          # 모듈의 전역 변수

def g1():
    print(X)                    # 모듈의 전역 변수를 참조한다(11)

def g2():
    global X
    X = 22                      # 모듈과 전역 변수를 생성한다

def h1():
    X = 33                      # 함수의 지역 변수
    def nested():
        print(X)                # 포함된 범위의 지역 변수를 참조한다(33)

def h2():
    X = 33                      # 함수의 지역 변수
    def nested():
        nonlocal X              # 파이썬 3.X 구문
        X = 44                  # 포함된 범위의 지역 변수를 수정한다

