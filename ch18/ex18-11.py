# 이제는 사라진 내장된 apply(파이썬 2.X)

func(*pargs, **kargs)           # 새로운 호출 구문: func(*시퀀스, **딕셔너리)
apply(func, pargs, kargs)       # 지금은 사라진 내장된: apply(func, 시퀀스, 딕셔너리)


def echo(*args, **kwargs): print(args, kwargs)

echo(1, 2, a=3, b=4)
# (1, 2) {'a': 3, 'b': 4}


pargs = (1, 2)
kargs ={'a':3, 'b':4}

apply(echo, pargs, kargs)
# (1, 2) {'a': 3, 'b': 4}

echo(*pargs, **kargs)
# (1, 2) {'a': 3, 'b': 4}


apply(pow, (2, 100))
# 1267650600228229401496703205376L
pow(*(2, 100))
# 1267650600228229401496703205376L


echo(0, c=5, *pargs, **kargs)   # 일반, 키워드, *시퀀스, **딕셔너리
# (0, 1, 2) {'c': 5, 'a': 3, 'b': 4}
