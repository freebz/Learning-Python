# 3.X의 bytes 객체 사용하기

# 메서드 호출

# py -3

# str에는 있지만 bytes에 없는 속성
set(dir('abc')) - set(dir(b'abc'))
# {'isnumeric', 'casefold', 'format', 'isidentifier', 'format_map', 'encode', 'isdecimal', 'isprintable'}

# bytes에는 있지만 str에 없는 속성
set(dir(b'abc')) - set(dir('abc'))
# {'decode', 'hex', 'fromhex'}


B = b'spam'                     # b'...' bytes 리터럴
B.find(b'pa')
# 1

B.replace(b'pa', b'XY')         # bytes 메서드는 bytes 인수를 받음
# b'sXYm'

B.split(b'pa')                  # bytes 메서드는 bytes로 결과 반환
# [b's', b'm']

B
# b'spam'
B[0] = 'x'
# TypeError: 'bytes' object does not support item assignment


'%s' % 99
# '99'
b'%s' % 99
# TypeError: %b requires a bytes-like object, or an object that implements __bytes__, not 'int'

'{0}'.format(99)
# '99'
b'{0}'.format(99)
# AttributeError: 'bytes' object has no attribute 'format'
