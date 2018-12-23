# 타입별 메서드

S = 'Spam'
S.find('pa')                    # S에서 부분 문자열의 오프셋을 찾음
# 1
S
# 'Spam'
S.replace('pa', 'XYZ')          # S에서 부분 문자열을 다른 문자열로 변경
# 'SXYZm'
S
# 'Spam'


line = 'aaa,bbb,ccccc,dd'
line.split(',')                 # 구문자로 분할하여 부분 문자열의 리스트 생성
# ['aaa', 'bbb', 'ccccc', 'dd']

S = 'spam'
S.upper()                       # 대소문자 변환
# 'SPAM'
S.isalpha()                     # 문자열 내용 테스트: isalpha, isdigit 등
# True
line = 'aaa,bbb,ccccc,dd\n'
line.rstrip()                   # 오른쪽 끝에서 공백 문자 제거
# 'aaa,bbb,ccccc,dd'
line.rstrip().split(',')        # 두 연산을 결합
# ['aaa', 'bbb', 'ccccc', 'dd']


'%s, eggs, and %s' % ('spam', 'SPAM!') # 포맷팅 표현식(모든 버전)
# 'spam, eggs, and SPAM!'

'{0}, eggs, and {1}'.format('spam', 'SPAM!') # 포매팅 메서드(2.6+, 3.0+)
# 'spam, eggs, and SPAM!'

'{}, eggs, and {}'.format('spam', 'SPAM!') # 인수 값 번호 생략(2.7+, 3.1+)
# 'spam, eggs, and SPAM!'


'{:,.2f}'.format(296999.2567)   # 구분자, 소수 자릿수
# '296,999.26'
'%.2f | %+05d' % (3.14159, -42) # 자릿수, 패팅, 기호
# '3.14 | -0042'
