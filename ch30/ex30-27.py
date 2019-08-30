# 함수 인터페이스와 콜백 기반 코드

class Callback:
    def __init__(self, color):      # 함수 + 상태 정보
        self.color = color
    def __call__(self):             # 인수가 없는 호출을 지원
        print('turn', self.color)


# 핸들러
cb1 = Callback('blue')          # blue 기억
cb2 = Callback('green')         # green 기억

B1 = Button(command=cb1)        # 핸들러 등록
B2 = Button(command=cb2)


# 이벤트
cb1()                           # 'turn blue' 출력
cb2()                           # 'gurn green' 출력


def callback(color):            # 유효 범위 vs. 속성
    def oncall():
        print('turn', color)
    return oncall

cb3 = callback('yellow')        # 핸들러는 등록되어야 함
cb3()                           # 이벤트 발생 시: 'turn yellow' 출력


cb4 = (lambda color='red': 'turn ' + color)    # 기본값도 상태 정보를 저장함
print(cb4())                                   # 'turn red'가 출력됨


class Callback:
    def __init__(self, color):          # 상태 정보를 갖는 클래스
        self.color = color
    def changeColor(self):              # 일반 명명된 메서드
        print('turn', self.color)

cb1 = Callback('blue')
cb2 = Callback('yellow')

B1 = Button(command=cb1.changeColor)    # 바운드 메서드: 참조할 뿐, 호출하지 않음
B2 = Button(command=cb2.changeColor)    # function + self 쌍을 기억함


cb1 = Callbakc('blue')
obj = cb1.changeColor                   # 등록된 이벤트 핸들러
obj()                                   # 이벤트 발생 시, 'turn blue' 출력
