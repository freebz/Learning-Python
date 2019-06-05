# 보너스 점수

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y # lambda, eval 또한 참고
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3)) # 테스트 코드
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))

# python minmax.py
# 1
# 6
