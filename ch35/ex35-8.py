# 맞춤형 데이터와 행위

# 예외 세부 내역 제공하기

class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file

def parser():
    raise FormatError(42, file='spam.txt')      # 에러가 발견된 경우

try:
    parser()
except FormatError as X:
    print('Error at: %s %s' % (X.file, X.line))

# Error at: spam.txt 42


class FormatError(Exception): pass              # 상속된 생성자

def parser():
    raise FormatError(42, 'spam.txt')           # 키워드 인수는 허용되지 않음!

try:
    parser()
except FormatError as X:
    print('Error at:', X.args[0], X.args[1])    # 이 애플리케이션에 특화되지 않음

# Error at: 42 spam.txt
