# 더 생각해 볼 주제: 람다 콜백

import sys
from tkinter import Button, mainloop # 2.X에서 Tkinter

x = Button(
    text='Press me',
    command=(lambda:sys.stdout.write('Spam\n'))) # 3.X: print()
x.pack()
mainloop()                      # 이 코드는 콘솔 모드에서는 선택 사항임


class MyGui:
    def makewidgets(self):
        Button(command=(lambda: self.onPress("spam")))
    def onPress(self, message):
        ...message 사용...
