# 예제: 함수 인수 검사하기

# 목표

class Person:
    ...
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Person:
    def giveRaise(self, percent):              # 인라인 코드로 검증
        if percent < 0.0 or percent > 1.0:
            raise TypeError, 'percent invalid'
        self.pay = int(self.pay * (1 + percent))

class Person:                                  # assert문을 이용한 검증
    def giveRaise(self, percent):
        assert percent >= 0.0 and percent <= 1.0, 'percent invalid'
        self.pay = int(self.pay * (1 + percent))


class Person:
    @rangetest(percent=(0.0, 1.0))      # 검증을 위해 데코레이터를 사용함
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
