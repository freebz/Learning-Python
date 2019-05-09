# 첫 번째 예제: 정의와 호출

# 정의

def times(x, y):                # 함수를 생성하고 할당
    return x * y                # 호출 시 실행되는 본문


# 호출

times(2, 4)                     # 괄호 안에 인수를 넣음
# 8


x = times(3.14, 4)              # 결과 객체를 저장함
x
# 12.56


times('Ni', 4)                  # 함수는 타입이 없음
# 'NiNiNiNi'
