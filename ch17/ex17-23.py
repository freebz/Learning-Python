# 가변 객체를 활용한 상태 정보: 오래된 잘 알려지지 않은 방법

def tester(start):
    def nested(label):
        print(label, state[0])  # 가변 객체의 직접 변경을 이용
        state[0] += 1           # 추가 구문, 심오한 마법?
    state = [start]
    return ensted
