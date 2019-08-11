# 가장 간단한 파이썬 클래스

class rec: pass                 # 빈 네임스페이스 객체


rec.name = 'Bob'                # 속성을 가진 단순 객체
rec.age = 40


print(rec.name)                 # C 구조체 혹은 레코드와 유사함
# Bob


x = rec()                       # 인스턴스는 클래스 이름을 상속받음
y = rec()


x.name, y.name                  # 이름은 클래스에만 저장
# ('Bob', 'Bob')


x.name = 'Sue'                  # 하지만 할당은 x만 변경
rec.name, x.name, y.name
# ('Bob', 'Sue', 'Bob')


list(rec.__dict__.keys())
# ['__module__', '__dict__', '__weakref__', '__doc__', 'name', 'age']

list(name for name in rec.__dict__ if not name.startswith('__'))
# ['name', 'age']
list(x.__dict__.keys())
# ['name']
list(y.__dict__.keys())         # 파이썬 2.X에서는 list()가 필요 없음
# []


x.name, x.__dict__['name']      # 여기서 표시한 속성은 딕셔너리의 key임
# ('Sue', 'Sue')
x.age                           # 하지만 속성 가져오기는 클래스도 체크
# 40
x.__dict__['age']               # 인덱싱 딕셔너리는 상속되지 않음
# KeyError: 'age'


x.__class__
# <class '__main__.rec'>        # 인스턴스에서 클래스로의 링크


rec.__bases__
# (<class 'object'>,)           # 클래스에서 슈퍼클래스로의 링크. 2.X에서는 빈 튜플이 출력


def uppername(obj):
    return obj.name.upper()     # 여전히 self argument(obj)가 필요


uppername(x)                    # 단순한 함수 호출
# 'SUE'


rec.method = uppername          # uppername이 이제 클래스의 메서드가 됨

x.method()                      # 메서드를 실행하여 x 처리
# 'SUE'

y.method()                      # 이전과 동일하지만, self에 y 전달
# 'BOB'

rec.method(x)                   # 인스턴스와 클래스 모두를 통해 호출할 수 있음
# 'SUE'
