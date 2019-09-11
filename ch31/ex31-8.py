# 메서드는 객체: 바운드 메서드와 언바운드 메서드

class Spam:
    def doit(self, message):
        print(message)


object1 = Spam()
object1.doit('hello world')


object1 = Spam()
x = object1.doit                # 바운드 메서드 객체: 인스턴스 + 함수
x('hello world')                # object1.doit('...')과 동일한 결과


object1 = Spam()
t = Spam.doit                   # 언바운드 메서드 객체(3.X에서의 함수: 앞으로 설명 예정)
t(object1, 'howdy')             # 인스턴스를 전달(3.X에서 메서드가 이를 기대한다면)


class Eggs:
    def m1(self, n):
        print(n)
    def m2(self):
        x = self.m1             # 다른 바운드 메서드 객체
        x(42)                   # 단순 함수로 보임

Eggs().m2()                     # 42 출력
