# 순서 규칙

def kwonly(a, **pargs, b, c):
# SyntaxError: invalid syntax
def kwonly(a, **, b, c):
# SyntaxError: invalid syntax


def f(a, *b, **d, c=6): print(a, b, c, d) # 키워드 전용은 ** 앞에!
# SyntaxError: invalid syntax

def f(a, *b, c=6, **d): print(a, b, c, d) # 헤더에서 인수 수집

f(1, 2, 3, x=4, y=5)            # 기본값 사용
# 1 (2, 3) 6 {'x': 4, 'y': 5}

f(1, 2, 3, x=4, y=5, c=7)       # 기본값 무시
# 1 (2, 3) 7 {'x': 4, 'y': 5}

f(1, 2, 3, c=7, x=4, y=5)       # 키워드만 있다면, 어디에서나 등장!
# 1 (2, 3) 7 {'x': 4, 'y': 5}

def f(a, c=6, *b, **d): print(a, b, c, d) # 여기서는 c는 키워드 전용이 아님!

f(1, 2, 3, x=4)
# 1 (3,) 2 {'x': 4}


def f(a, *b, c=6, **d): print(a, b, c, d) # *와 **사이에 키워드 전용 인수

f(1, *(2, 3), **dict(x=4, y=5)) # 호출 시 인수를 언패킹
# 1 (2, 3) 6 {'x': 4, 'y': 5}

f(1, *(2, 3), **dict(x=4, y=5), c=7) # **args 앞에 키워드 인수!
# SyntaxError: invalid syntax        # 3.5부터는 인수 순서 규칙의 완화로 지원

f(1, *(2, 3), c=7, **dict(x=4, y=5)) # 기본값 무시
# 1 (2, 3) 7 {'x': 4, 'y': 5}

f(1, c=7, *(2, 3), **dict(x=4, y=5)) # *앞이나 뒤에 위치
# 1 (2, 3) 7 {'x': 4, 'y': 5}

f(1, *(2, 3), **dict(x=4, y=5, c=7)) # ** 안에 키워드 전용 인수 사용
# 1 (2, 3) 7 {'x': 4, 'y': 5}
