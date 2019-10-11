# 2.X에서 문자열 타입 혼용하기

u'ab' + 'cd'                    # 2.X에서 호환될 경우 혼용 가능함
# u'abcd'                       # 'ab' + b'cd'는 3.X에서 허용되지 않음


S = 'A\xC4B\xE8C'               # 2.X에서는 문자열이 아스키가 아닌 경우 혼용 불가능함
U = u'A\xC4B\xE8C'
S + U
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 1: ordinal not in range(128)

'abc' + U                       # 문자열이 모두 7비트 아스키인 경우에만 혼용 가능함
# u'abcA\xc4B\xe8C'
print 'abc' + U                 # print를 이용해 문자 출력
# abcAÄBèC

S.decode('latin-1') + U         # 2.X에서도 수동 변환 필요
# u'A\xc4B\xe8CA\xc4B\xe8C'
print S.decode('latin-1') + U
# AÄBèCAÄBèC

print u'\xA3' + '999.99'        # 25장의 통화 예제 참조
# £999.99


str(u'spam')                    # 유니코드 -> 일반
# 'spam'
unicode('spam')                 # 일반 -> 유니코드
# u'spam'
