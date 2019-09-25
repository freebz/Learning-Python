# 가변 클래스 속성 변경도 부작용을 가질 수 있음

class C:
    shared = []                 # 클래스 속성
    def __init__(self):
        self.perobj = []        # 인스턴스 속성

x = C()                         # 두 개의 인스턴스
y = C()                         # 암묵적으로 클래스 속성을 공유
y.shared, y.perobj
# ([], [])

x.shared.append('spam')         # y의 관점에도 영향을 줌!
x.perobj.append('spam')         # x의 데이터에만 영향을 줌
x.shared, x.perobj
# (['spam'], ['spam'])


y.shared, y.perobj              # y는 x를 통해 변경된 값을 봄
# (['spam'], [])
C.shared                        # 클래스에 저장되고 공유됨
# ['spam']


x.shared.append('spam')         # 클래스에 첨부된 공유 객체를 직접 변경
x.shared = 'spam'               # x에 첨부된 인스턴스 속성을 변경하거나 또는 생성
