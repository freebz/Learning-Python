# 불리안 테스트: __bool__과 __len__

class Truth:
    def __bool__(self): return True

X = Truth()
if x: print('yes!')

# yes!

class Truth:
    def __bool__(self): return False

X = Truth()
bool(X)
# False


class Truth:
    def __len__(self): return 0

X = Truth()
if not X: print('no!')

# no!


class Truth:
    def __bool__(self): return True     # 3.X에서는 __bool__을 먼저 시도
    def __len__(self): return 0         # 2.X에서는 __len__을 먼저 시도

X = Truth()
if X: print('yes!')

# yes!


class Truth:
    pass

X = Truth()
bool(X)
# True
