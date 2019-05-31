# 실제 동작하는 nonlocal

# c:\python36\python

def tester(start):
    state = start               # 일반적으로 비지역 변수의 참조는 가능함
    def nested(label):
        print(label, state)     # 바깥쪽 범위의 상태를 기억함
    return nested

F = tester(0)
F('spam')
# spam 0
F('ham')
# ham 0


def tester(start):
    state = start
    def nested(label):
        print(label, state)
        state += 1              # 기본적으로 변경 불가(2.X에서는 절대 불가)
    return nested

F = tester(0)
F('spam')
# UnboundLocalError: local variable 'state' referenced before assignment
