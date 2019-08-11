# 세 번째 예제

class ThirdClass(SecondClass):  # SecondClass로부터 상속
    def __init__(self, value):  # "ThirdClass(value)" 호출 시
        self.data = value
    def __add__(self, other):   # "self + other" 호출 시
        return ThirdClass(self.data + other)
    def __str__(self):          # "print(self)"나 "str()" 호출 시
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):
        self.data *= other

a = ThirdClass('abc')           # __init__ 홏ㄹ됨
a.display()                     # 상속 메서드 호출됨
# Current value = "abc"
print(a)                        # str: 디스플레이 문자열 반환
# [ThirdClass: abc]

b = a + 'xyz'                   # add: 새 인스턴스 생성
b.display()                     # b는 ThirdClass의 모든 메서드를 가짐
# Current value = "abcxyz"
print(b)                        # str: 디스플레이 문자열 반환
# [ThirdClass: abcxyz]

a.mul(3)                        # mul: 인스턴스 변경
print(a)
# [ThirdClass: abcabcabc]
