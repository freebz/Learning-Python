# 함수 주의 사항

# 지역 이름들은 정적으로 감지됨

X = 99

def selector():                 # X가 사용되지만 할당되지는 않음
    print(X)                    # X는 전역 범위에서 검색됨

selector()


def selector():                 # 아직 존재하지 않는다!
    print(X)                    # X는 모든 지역에서 지역 이름으로 분류됨
    X = 88                      # "import X", "def X"의 경우에도 발생할 수 있음

selector()
# UnboundLocalError: local variable 'X' referenced before assignment


def selector():
    global X                    # X를 강제로 전역으로 만듦
    print(X)
    X = 88

selector()
# 99


X = 99
def selector():
    import __main__             # 바깥쪽 모듈 임포트
    print(__main__.X)           # 전역 버전의 이름 구하기
    X = 88                      # 여기서 X는 지역으로 분류
    print(X)                    # 지역 버전의 이름 출력

selector()
# 99
# 88
