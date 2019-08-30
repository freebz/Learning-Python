# 파이썬 2.X에서의 불리안 메서드

# py -3
class C:
    def __bool__(self):
        print('in bool')
        return False

X = C()
bool(X)
# in bool
# False
if X: print(99)

# in bool


# py -2
class C:
    def __bool__(self):
        print('in bool')
        return False

X = C()
bool(X)
# True
if X: print(99)

# 99


# py -2
class C:
    def __nonzero__(self):
        print('in nonzero')
        return False            # 정수값 반환(또는 True/False, 1/0과 동일)

X = C()
bool(X)
# in nonzero
# False
if X: print(99)

# in nonzero
