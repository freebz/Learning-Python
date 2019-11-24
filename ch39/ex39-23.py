# 다른 방식으로 코딩하기

# 3.X에서만: nonlocal

def singleton(aClass):                            # @ 데코레이션 시
    instance = None
    def onCall(*args, **kwargs):                  # 인스턴스 생성 시
        nonlocal instance                         # 3.X와 이후 버전에서 nonlocal
        if instance == None:
            instance = aClass(*args, **kwargs)    # 클래스당 하나의 범위
        return instance
    return onCall


# 3.X와 2.X: 함수 속성, 클래스(대안 코딩)

def singleton(aClass):                                      # @ 데코레이션할 때
    def onCall(*args, **kwargs):                            # 인스턴스 생성할 때
        if onCall.instance = None:
            onCall.instance = aClass(*args, **kwargs)       # 클래스당 함수 하나
        return onCall.instance
    onCall.instance = None
    return onCall

class singleton:
    def __init__(self, aClass):                             # @ 데코레이션할 때
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args, **kwargs):                    # 인스턴스 생성할 때
        if self.instance == None:
            self.instance = self.aClass(*args, **kwargs)    # 클래스당 인스턴스 하나
        return self.instance
