# 객체 폐기: __del__

class Life:
    def __init__(self, name='unknown'):
        print('Hello ' + name)
        self.name = name
    def live(self):
        print(self.name)
    def __del__(self):
        print('Goodbye ' + self.name)

brian = Life('Brian')
# Hello Brian
brian.live()
# Brian
brian = 'loretta'
# Goodbye Brian
