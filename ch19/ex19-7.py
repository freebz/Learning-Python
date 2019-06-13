# 함수 객체: 속성과 어노테이션

# 간접 함수 호출: '퍼스트 클래스' 객체

def echo(message):              # 이름 echo에 함수 객체가 할당됨
    print(message)

echo('Direct call')             # 원래 이름을 통한 객체 호출
# Direct call

x = echo                        # 이제 x 또한 함수를 참조함
x('Indirect call!')             # ()를 추가하여 이름을 통한 객체 호출
# Indirect call!


def indirect(func, arg):
    func(arg)                   # 전달된 객체에 ()를 추가하여 호출

indirect(echo, 'Argument call!') # 함수를 또 다른 함수에 전달
# Argument call!


schedule = [ (echo, 'Spam!'), (echo, 'Ham!') ]
for (func, arg) in schedule:
    func(arg)                   # 컨테이너에 포함된 함수 호출

# Spam!
# Ham!


def make(label):                # 함수를 만들지만 호출하지는 않음
    def echo(message):
        print(label + ':' + message)
    return echo

F = make('Spam')                # 바깥쪽 범위에 있는 label은 유지됨
F('Ham!')                       # 반환된 함수 호출
# Spam:Ham!
F('Eggs!')
# Spam:Eggs!
