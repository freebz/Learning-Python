# 팩토리 함수: 클로저

# 단순한 함수 팩토리

def maker(N):
    def action(X):              # action을 만들고 반환함
        return X ** N           # action은 바깥쪽 범위의 N을 유지함
    return action


f = maker(2)                    # N의 인수로 2를 넘겨줌
f
# <function maker.<locals>.action at 0x7fe298596400>


f(3)                            # 3을 X에 전달. N이 2를 기억하므로 3 ** 2
# 9
f(4)                            # 4 ** 2
# 16


g = maker(3)                    # g는 3을 기억하고, f는 2를 기억함
g(4)                            # 4 ** 3
# 64
f(4)                            # 4 ** 2
# 16


def maker(N):
    return lambda X: X ** N     # lambda 함수도 상태를 기억함

h = maker(3)
h(4)                            # 다시 4 ** 3
# 64
