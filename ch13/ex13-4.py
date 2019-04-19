# pass

while True: pass                # 멈추기 위해서는 Ctrl + C 입력


def func1():
    pass                        # 실제 코드를 나중에 여기다 추가

def func2():
    pass


def func1():
    ...                         # pass의 또 다른 방법

def func2():
    ...

func1()                         # 호출하면 아무 일도 하지 않음


def func1(): ...                # 헤더 라인에서도 동작함
def func2(): ...
X = ...                         # None을 대체할 수 있음
X
