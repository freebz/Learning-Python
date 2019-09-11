# 사용 변형: 더 큰 모듈에서 실행하기

from listtree import ListTree
from tkinter import Button                # 두 클래스 모두 __str__을 가짐
class MyButton(ListTree, Button): pass    # ListTree 먼저: 이것의 __str__ 사용

B = MyButton(text='spam')
open('savetree.txt', 'w').write(str(B))   # 나중에 볼 수 있도록 파일에 저장
# 20513
len(open('savetree.txt').readlines())     # 파일의 줄 수
# 330
print(B)                                  # 디스플레이를 여기에 출력
# <Instance of MyButton, address 140013880934296:
#  _ListTree__visited={}
#  _name=!mybutton
#  _tclCommands=None
#  _w=.!mybutton
#  children={}
#  master=.
#  ...출력의 상당 부분이 생략됨...
# >
S = str(B)                                # 또는 단지 첫 부분만 출력
print(S[:1000])
