# 범위 예제

# 전역 범위
X = 99                          # X와 func가 모듈 내에 할당됨: 전역

def func(Y):                    # Y와 Z는 함수 내에 할당됨: 지역
    # 지역 범위
    Z = X + Y                   # X는 전역
    return Z

func(1)                         # 모듈 내의 func: 결과값 = 100
