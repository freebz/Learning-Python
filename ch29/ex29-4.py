# 메서드 예제

class NextClass:                # 클래스 정의
    def printer(self, text):    # 메서드 정의
        self.message = text     # 인스턴스 변경
        print(self.message)     # 인스턴스 접근


x = NextClass()                 # 인스턴스 생성
x.printer('instance call')      # 생성한 인스턴스의 메서드 호출
# instance call
x.message                       # 변경된 인스턴스
# 'instance call'


NextClass.printer(x, 'class call')    # 직접 클래스 호출
# class call
x.message                             # 인스턴스가 다시 변경됨
# 'class call'


NextClass.printer('bad call')
# TypeError: unbound method printer() must be called with NextClass instance...
