# 왜 디스플레이 메서드가 두 개인가?

class addstr(adder):
    def __str__(self):                            # __str__ but no __repr__
        return '[Value: %s]' % self.data          # 보기 좋은 문자열로 변환

x = addstr(3)
x + 1
x                                                 # 기본은 __repr__
# <__main__.addstr object at 0x7f351075d860>
print(x)                                          # __str__ 실행
# [Value: 4]
str(x), repr(x)
# ('[Value: 4]', '<__main__.addstr object at 0x7f351075d860>')


class addboth(adder):
    def __str__(self):
        return '[Value: %s]' % self.data          # 사용자 친화적인 문자열
    def __repr__(self):
        return 'addboth(%s)' % self.data          # 코드대로의 문자열

x = addboth(4)
x + 1
x                                                 # __repr__ 실행
# addboth(5)
print(x)                                          # __str__ 실행
# [Value: 5]
str(x), repr(x)
# ('[Value: 5]', 'addboth(5)')
