# 더 큰 작업 처리하기

def function(): ...
def default(): ...

branch = {'spam': lambda: ...,
          'ham': function,
          'eggs': lambda: ...}

branch.get(choice, default)()
