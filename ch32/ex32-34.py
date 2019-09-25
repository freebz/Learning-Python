# 위험 요소: 순진하게 다중 상속을 추가하기

class A:                        # 파이썬 3.X
    def act(self): print('A')
class B:
    def act(self): print('B')
class C(A):
    def act(self):
        super().act()           # super는 단일 상속 트리에 적용
X = C()
X.act()


class C(A, B):                  # 동일 메서드에 클래스 B를 섞어서 추가함
    def act(self):
        super().act()           # 다중 상속에서 실패하진 않지만, 딱 하나만 선택!
X = C()
X.act()
# A

class C(B, A):
    def act(self):
        super().act()           # B가 처음에 나왔다면, A.act()는 더 이상 실행되지 않음!
X = C()
X.act()
# B


class C(A, B):                  # 전형적인 형태
    def act(self):              # 여기에서 보다 명확할 필요가 있음
        A.act(self)             # 이 형태는 단일 이름, 다중 상속 모두를 처리
        B.act(self)             # 파이썬 3.X와 2.X에서 동일하게 동작
X = C()                         # 그렇다면 도대체 왜 super()를 사용하는가?
X.act()
# A
# B


class PyMailServerWindow(PyMailServer, windows.MainWindow):
    "a Tk, with extra protocol and mixed-in methods"
    def __init__(self):
        windows.MainWindow.__init__(self, appname, srvrname)
        PyMailServer.__init__(self)

class PyMailFileWindow(PyMailFile, windows.PopupWindow):
    "a Toplevel, with extra protocol and mixed-in methods"
    def __init__(self, filename):
        windows.PopupWindow.__init__(self, appname, filename)
        PyMailFile.__init__(self, filename)
