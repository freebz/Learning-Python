# bytes 객체를 만드는 다른 방법

B = b'abc'                      # 리터럴
B
# b'abc'

B = bytes('abc', 'ascii')       # 생성자에 인코딩 이름 전달
B
# b'abc'

ord('a')
# 97
B = bytes([97, 98, 99])         # 정수 반복
B
# b'abc'

B = 'spam'.encode()             # str.encode()(또는 bytes())
B
# b'spam'

S = B.decode()                  # bytes.decode()(또는 str())
S
# 'spam'
