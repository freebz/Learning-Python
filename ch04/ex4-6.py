# 문자열을 작성하는 다른 방법들

S = 'A\nB\tC'                   # \n은 라인의 끝, \t는 탭을 의미
len(S)                          # 각각은 한 문자를 나타냄
# 5

ord('\n')                       # \n은 십진수 값 10인 하나의 문자
# 10

S = 'A\0B\0C'                   # \0, 바이너리 값이 0인 바이트, 문자열을 종료하지 않음
len(S)
# 5
S                               # 출력할 수 없는 문자는 \NN 16진수 이스케이프로 출력됨
# 'A\x00B\x00C'


msg = """
aaaaaaaaaaaaa
bbb'''bbbbbbbbbb""bbbbbb'bbbb
cccccccccccccc
"""
msg
# '\naaaaaaaaaaaaa\nbbb\'\'\'bbbbbbbbbb""bbbbbb\'bbbb\ncccccccccccccc\n'
