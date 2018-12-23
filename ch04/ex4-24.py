# 코드의 유연성을 깨트리는 방법

# 파이썬 2.X
type(L)                         # 타입: L의 타입은 리스트 타입 객체
# <type 'list'>
type(type(L))                   # 심지어 type도 객체
# <type 'type'>

# 파이썬 3.X
type(L)                         # 3.X: 타입은 클래스이며, 반대도 마찬가지
# <class 'list'>
type(type(L))                   # 클래스 타입에 대해서는 32장 참조
# <class 'type'>


if type(L) == type([]):         # 타입 테스트
    print('yes')

# yes
if type(L) == list:             # 타입 이름을 이용한 테스트
    print('yes')

# yes
if isinstance(L, list):         # 객체에 기반한 테스트
    print('yes')

# yes
