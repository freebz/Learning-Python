# -*- coding: utf-8 -*-
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
