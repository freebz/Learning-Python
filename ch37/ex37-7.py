# 아스키가 아닌 텍스트 코딩하기

chr(0xc4)                       # 0xC$, 0xE8: 아스키 범위 밖의 문자 집합
# 'Ä'
chr(0xe8)
# 'è'

S = '\xc4\xe8'                  # 단일 8비트 값 16진수 이스케이프 문자: 두 개의 숫자로 구성됨
S
# 'Äè'

S = '\u00c4\u00e8'              # 16비트 유니코드 이스케이프 문자: 네 개의 숫자로 구성됨
S
# 'Äè'
len(S)                          # 두 글자 길이(바이트 숫자가 아님!)
# 2


S = '\U000000c4\U000000e8'      # 32비트 유니코드 이스케이프 문자: 각각 여덟 개의 숫자로 구성됨
S
# 'Äè'
