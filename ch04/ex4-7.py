# 유니코드 문자열

'sp\xc4m'                       # 3.X에서 일반적인 str 문자열은 유니코드 텍스트
# 'spÄm'
b'a\x01c'                       # 바이트 문자열은 바이트 기반 데이터
# b'a\x01c'
u'sp\u00c4m'                    # 2.X 유니코드 리터럴은 3.3+에서 str처럼 동작
# 'spÄm'


print u'sp\xc4m'                # 2.X에서 유니코드 문자열은 별도의 타입임
# spÄm
'a\x01c'                        # 일반적인 str 문자열은 바이트 기반의 텍스트/데이터를 포함하고 있음
# 'a\x01c'
b'a\x01c'                       # 3.X 바이트 리터럴은 2.6+에서 str처럼 동작함
# 'a\x01c'


'spam'                          # 문자들은 메모리에 1, 2 또는 4바이트로 저장됨
# 'spam'
'spam'.encode('utf8')           # UTF-8 형식의 4바이트로 인코딩됨
# b'spam'
'spam'.encode('utf16')          # UTF-16 형식의 10바이트로 인코딩됨
# b'\xff\xfes\x00p\x00a\x00m\x00'


'sp\xc4\u00c4\U000000c4m'
# 'spÄÄÄm'


'\u00A3', '\u00A3'.encode('latin1'), b'\xA3'.decode('latin1')
# ('£', b'\xa3', '£')


u'x' + b'y'                     # 2.X에서 동작(b는 선택 사항이며 생략 가능)
u'x' + 'y'                      # 2.X에서 동작: u'xy'

u'x' + b'y'                     # 3.6에서 동작하지 않음 (u는 선택 사항이며 생략 가능)
u'x' + 'y'                      # 3.6에서 동작: 'xy'

'x' + b'y'.decode()             # 3.X에서 bytes를 str로 디코딩 후 동작: 'xy'
'x'.encode() + b'y'             # 3.X에서 str을 bytes로 인코딩 후 동작: b'xy'
