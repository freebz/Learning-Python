# 영역 문제

def tester(start):
    def nested(label):
        nonlocal state          # 비지역은 바깥쪽 def에 미리 존재해야 함!
        state = 0
        print(label, state)
    return nested

# SyntaxError: no binding for nonlocal 'state' found

def tester(start):
    def nested(label):
        global state            # 전역은 선언 전에 미리 정의되지 않아도 됨
        state = 0               # 이 코드는 지금 모듈 범위에 이름을 만듦
        print(label, state)
    return nested

F = tester(0)
F('abc')
# abc 0
state
# 0


spam = 99
def tester():
    def nested():
        nonlocal spam           # 모듈이 아닌 def 내에 존재해야 한다!
        print('Current=', spam)
        spam += 1
    return nested

# SyntaxError: no binding for nonlocal 'spam' found
