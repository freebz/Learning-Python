# pickle 객체 직렬화 모듈

# py -3
import pickle                           # dumps() 는 피클 문자열을 반환

pickle.dumps([1, 2, 3])                 # 파이썬 3.X의 기본 프로토콜 = 3 = 바이너리
# b'\x80\x03]q\x00(K\x01K\x02K\x03e.'

pickle.dumps([1, 2, 3], protocol=0)     # ASCII protocol 0, 하지만 여전히 바이트
# b'(lp0\nL1L\naL2L\naL3L\na.'


pickle.dump([1, 2, 3], open('temp', 'w'))     # bytes에서는 텍스트 파일 오픈 불가
# TypeError: must be str, not bytes           # 프로토콜 값과 상관없음

pickle.dump([1, 2, 3], open('temp', 'w'), protocol=0)
# TypeError: write() argument must be str, not bytes

pickle.dump([1, 2, 3], open('temp', 'wb'))    # 3.X에서는 언제나 바이너리 모드

open('temp', 'r').read()                      # 이 코드는 동작하지만, 우연일 뿐임
# '\u20ac\x03]q\x00(K\x01K\x02K\x03e.'
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte


pickle.dump([1, 2, 3], open('temp', 'wb'))
pickle.load(open('temp', 'rb'))
# [1, 2, 3]
open('temp', 'rb').read()
# b'\x80\x03]q\x00(K\x01K\x02K\x03e.'


# py -2
import pickle
pickle.dumps([1, 2, 3])                       # 파이썬 2.X 기본 = 0 = ASCII
# '(lp0\nI1\naI2\naI3\na.'

pickle.dumps([1, 2, 3], protocol=1)
# ']q\x00(K\x01K\x02K\x03e.'

pickle.dump([1, 2, 3], open('temp', 'w'))     # 2.X에서는 텍스트 모드도 사용 가능함
pickle.load(open('temp'))
# [1, 2, 3]
open('temp').read()
# '(lp0\nI1\naI2\naI3\na.'


import pickle
pickle.dump([1, 2, 3], open('temp', 'wb'))    # 버전 중립적
pickle.load(open('temp', 'rb'))               # 3.X에서는 필수적임
# [1, 2, 3]
