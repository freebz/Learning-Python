# 다중 상속: '혼합(Mix-in)' 클래스들

# 혼합 디스플레이 클래스 코딩하기

class Spam:
    def __init__(self):                       # __repr__이나 __str__이 아님
        self.data1 = "food"
X = Spam()
print(X)                                      # 기본: 클래스명 + 주소(id)
# <__main__.Spam object at 0x7f80094acb38>    # 2.X에서는 동일, 하지만 'instance'라 말함
