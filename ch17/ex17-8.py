# 전역 변수에 접근하는 다른 방법들

# thismod.py

var = 99                        # 전역 변수 == 모듈 속성

def local():
    var = 0                        # 지역 변수 var 변경

def glob1():
    global var                      # 전역 변수 선언(일반적인 방식)
    var += 1                        # 전역 변수 var 변경

def glob2():
    var = 0                         # 지역 변수 var 변경
    import thismod                  # 자신을 임포트
    thismod.var += 1                # 전역 변수 var 변경

def glob3():
    var = 0                         # 지역 변수 var 변경
    import sys                      # 시스템 테이블 임포트
    glob = sys.modules['thismod']   # 모듈 객체 가져오기(또는 __name__ 사용)
    glob.var += 1                   # 전역 변수 var 변경

def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)


import thismod
thismod.test()
# 99
# 102
thismod.var
# 102
