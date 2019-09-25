# 새 형식 클래스 확장 도구들

# 슬롯: 속성 선언

# 슬롯의 기본

class limiter(object):
    __slots__ = ['age', 'name', 'job']

x = limiter()
x.age                           # 사용하기 전에 할당해야 함
# AttributeError: age
x.age = 40                      # 인스턴스 데이터로 보임
x.age
# 40
x.ape = 1000                    # 오류: __slots__에 없는 속성임
# AttributeError: 'limiter' object has no attribute 'ape'
