# 3.X에서 함수 어노테이션

def func(a, b, c):
    return a + b + c

func(1, 2, 3)
# 6


def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c

func(1, 2, 3)
# 6


func.__annotations__
# {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}


def func(a: 'spam', b, c: 99):
    return a + b + c

func(1, 2, 3)
# 6
func.__annotations__
# {'a': 'spam', 'c': 99}

for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])

# a => spam
# c => 99


def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c

func(1, 2, 3)
# 6
func()                          # 4 + 5 + 6(셋 모두 기본값)
# 15
func(1, c=10)                   # 1 +5 + 10(키워드 정상 동작)
# 16
func.__annotations__
# {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}


def func(a:'spam'=4, b:(1,10)=5, c:float=6)->int:
    return a + b + c

func(1, 2)                      # 1 + 2 + 6
# 9
func.__annotations__
# {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}
