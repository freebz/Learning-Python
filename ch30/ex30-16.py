# 속성 접근: __getattr__와 __setattr__

# 속성 참조

class Empty:
    def __getattr__(self, attrname):    # self.undefined일 때
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)

X = Empty()
X.age
# 40
X.name
# ..에러 구문 생략...
# AttributeError: name

