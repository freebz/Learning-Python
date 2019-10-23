# __getattribute__ 사용하기

# __getattr__을 이 코드로 대체

    def __getattribute__(self, attr):                 # 객체의 모든 속성에 대해 동작함
        print('get: ' + attr)
        if attr == 'name':                            # 모든 이름을 가로챔
            attr = '_name'                            # 내부 이름에 매핑
        return object.__getattribute__(self, attr)    # 루핑 방지


# py -3 getattribute-person.py
# set: _name
# get: __dict__
# get: name
# Bob Smith
# set: name
# get: __dict__
# get: name
# Robert Smith
# del: name
# get: __dict__
# --------------------
# set: _name
# get: __dict__
# get: name
# Sue Jones
