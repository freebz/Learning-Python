# 호출: 인수들 언패킹하기

def func(a, b, c, d): print(a, b, c, d)

args = (1, 2)
args += (3, 4)
func(*args)                     # func(1, 2, 3, 4)과 같음
# 1 2 3 4


args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func(**args)                    # func(a = 1, b = 2, c = 3, d = 4)과 같음
# 1 2 3 4


func(*(1, 2), **{'d': 4, 'c': 3}) # func(1, 2, d = 4, c = 3)와 같음
# 1 2 3 4
func(1, *(2, 3), **{'d': 4})    # func(1, 2, 3, d = 4)와 같음
# 1 2 3 4
func(1, c=3, *(2,), **{'d': 4}) # func(1, 2, c = 3, d = 4)와 같음
# 1 2 3 4
func(1, *(2,), c=3, **{'d':4})  # func(1, 2, c = 3, d = 4)와 같다
# 1 2 3 4
