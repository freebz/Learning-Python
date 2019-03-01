# 확장 슬라이싱: 세 번째 제약과 슬라이스 객체

S = 'abcdefghijklmnop'
S[1:10:2]                       # 아이템 건너뛰기
# 'bdfhj'
S[::2]
# 'acegikmo'


S = 'hello'
S[::-1]                         # 아이템 뒤집기
# 'olleh'


S = 'abcdefg'
S[5:1:-1]                       # 경계의 역할이 다름
# 'fedc'


'spam'[1:3]                     # 슬라이싱 구문
# 'pa'
'spam'[slice(1, 3)]             # 인덱스 구문을 사용한 슬라이스 객체
# 'pa'
'spam'[::-1]
# 'maps'
'spam'[slice(None, None, -1)]
# 'maps'


# echo.py 파일
import sys
print(sys.argv)

# % python echo.py -a -b -c
# ['echo.py', '-a', '-b', '-c']
