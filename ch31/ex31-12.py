# 더 생각해 볼 주제: 바운드 메서드 콜백

def handler():
    ...상태 정보를 위해 전역 또는 클로저 범위 사용...

...
widget = Button(text='spam', command=handler)


class MyGui:
    def handler(self):
        ...상태 정보를 위해 self.attr 사용...
    def makewidgets(self):
        b = Button(text='spam', command=self.handler)
