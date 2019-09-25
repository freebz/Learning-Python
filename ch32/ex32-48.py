# 메서드와 클래스에서의 범위

def generate():
    class Spam:                 # Spam은 generate의 지역 범위에 있는 이름
        count = 1
        def method(self):
            print(Spam.count)   # generate의 범위에 보이며, LEGB에서 E에 해당
    return Spam()

generate().method()


def generate():
    return Spam()

class Spam:                     # 모듈의 최상위 레벨에서 정의
    count = 1
    def method(self):
        print(Spam.count)       # 동작 가능: 전역 범위(모듈 범위)

generate().method()


def generate(label):            # 인스턴스 대신 클래스 반환
    class Spam:
        count = 1
        def method(self):
            print("%s=%s" % (label, Spam.count))
    return Spam

aclass = generate('Gotchas')
I = aclass()
I.method()
# Gotchas=1
