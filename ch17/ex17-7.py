# 프로그램 설계: 파일 간 변경을 최소화하기

# first.py
X = 99                          # 이 코드는 second.py를 모름

# second.py
import first
print(first.X)                  # OK: 다른 파일의 이름을 참조함
first.X = 88                    # 하지만 이 값의 변경은 너무 암묵적이고 미묘함


# first.py
X = 99

def setX(new):                  # 접근자는 외부 접근을 명시적으로 만들며
    global X                    # 한 곳에서 접근을 관리할 수 있음
    X = new

# second.py
import first
first.setX(88)                  # 직접 값을 변경하는 대신 함수를 호출함
