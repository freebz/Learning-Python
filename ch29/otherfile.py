# -*- coding: utf-8 -*-
# otherfile.py

import manynames

X = 66
print(X)                        # 66: 여기까지는 지역 변수
print(manynames.X)              # 11: 임포트 이후 X는 속성이 됨

manynames.f()                   # 11: manynames의 X
manynames.g()                   # 22: 다른 파일의 함수에 있는 지역 변수
print(manynames.C.X)            # 33: 다른 모듈 내의 클래스 속성임
I = manynames.C()
print(I.X)                      # 33: 여기까지는 아직 클래스의 속성임
I.m()
print(I.X)                      # 55: 이제 인스턴스의 속성임
