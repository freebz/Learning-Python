# 메서드 확장하기: 나쁜 방법

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        self.pay = int(self.pay * (1 + percent + bonus))    # 나쁜 방법: 복사/붙여넣기
