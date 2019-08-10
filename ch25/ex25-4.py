# __name__을 이용한 단위 테스트

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3)) # 셀프 테스트 코드
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))


print('I am:', __name__)

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

if __name__ == '__main__':
    print(minmax(lessthan, 4, 2, 1, 5, 6, 3)) # 셀프 테스트 코드
    print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))


# python minmax2.py
# I am: __main__
# 1
# 6


# python
import minmax2
# I am: minmax2
minmax2.minmax(minmax2.lessthan, 's', 'p', 'a', 'a')
# 'a'
