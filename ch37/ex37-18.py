# 문자열 타입 혼용하기

# 함수와 메서드 호출 시 적절한 타입을 전달해야 함

B = b'spam'

B.replace('pa', 'XY')
# TypeError: a bytes-like object is required, not 'str'

B.replace(b'pa', b'XY')
# b'sXYm'

B = B'spam'
B.replace(bytes('pa'), bytes('xy'))
# TypeError: string argument without an encoding

B.replace(bytes('pa', 'ascii'), bytes('xy', 'utf-8'))
# b'sxym'

# 3.X의 혼합 타입 표현식에서는 반드시 수동으로 변환해야 함

b'ab' + 'cd'
# TypeError: can't concat str to bytes

b'ab'.decode() + 'cd'           # bytes를 문자열로 변환
# 'abcd'
b'ab' + 'cd'.encode()           # 문자열을 bytes로 변환
# b'abcd'
b'ab' + bytes('cd', 'ascii')    # 문자열을 bytes로 변환
# b'abcd'
