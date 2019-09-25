# -*- coding: utf-8 -*-
# testmixin0.py 파일
from listinstance import ListInstance    # lister 도구 클래스 가져오기

class Super:
    def __init__(self):                  # 슈퍼클래스의 __init__
        self.data1 = 'spam'              # 인스턴스 속성 생성
    def ham(self):
        pass

class Sub(Super, ListInstance):          # ham과 __str__을 혼합
    def __init__(self):                  # Lister는 self에 접근할 수 없음
        Super.__init__(self)
        self.data2 = 'eggs'              # 더 많은 인스턴스 속성들
        self.data3 = 42
    def spam(self):                      # 여기에서 다른 메서드 정의
        pass

if __name__ == '__main__':
    X = Sub()
    print(X)                             # 혼합 __str__을 실행
