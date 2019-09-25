# 정적 메서드와 클래스 메서드 사용하기

# bothmethods.py 파일

class Methods:
    def imeth(self, x):         # 일반 인스턴스 모드: self를 전달
        print([self, x])

    def smeth(x):               # Static: 인스턴스를 전달하지 않음
        print([x])

    def cmeth(cls, x):          # Class: 인스턴스가 아니라 클래스를 취함
        print([cls, x])

    smeth = staticmethod(smeth) # smeth를 static 메서드로(또는 @. 이후 내용 참조)
    cmeth = classmethod(cmeth)  # cmeth를 class 메서드로(또는 @, 이후 내용 참조)


from bothmethods import Methods         # 일반 인스턴스 메서드
obj = Methods()                         # 인스턴스 또는 클래스를 통해 호출 가능
obj.imeth(1)
# [<bothmethods.Methods object at 0x7ff50c338160>, 1]
Methods.imeth(obj, 2)
# [<bothmethods.Methods object at 0x7ff50c338160>, 2]


Methods.smeth(3)                        # 정적 메서드: 클래스를 통해 호출
# [3]                                   # 인스턴스가 전달되지도, 이를 기대하지도 않음
obj.smeth(4)                            # 정적 메서드: 인스턴스를 통해 호출
# [4]                                   # 인스턴스가 전달되지 않음


Methods.cmeth(5)                        # Class 메서드: 클래스를 통해 호출
# [<class 'bothmethods.Methods'>, 5]    # cmeth(Methods, 5)와 동일
obj.cmeth(6)                            # Class 메서드: 인스턴스를 통해 호출
# [<class 'bothmethods.Methods'>, 6]    # cmeth(Methods, 6)와 동일
