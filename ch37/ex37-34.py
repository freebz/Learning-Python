# 3.X의 다른 문자열 도구 변경 사항

# re 패턴 매칭 모듈

# py -3
import re
S = 'Bugger all down here on earth!'              # 텍스트 라인
B = b'Bugger all down here on earth!'             # 보통은 파일에서 읽어 들임

re.match('(.*) down (.*) on (.*)', S).groups()    # 라인을 패턴에 매치시킴
# ('Bugger all', 'here', 'earth!')                # 매치된 서브 문자열

re.match(b'(.*) down (.*) on (.*)', B).groups()   # 바이트 서브 문자열
# (b'Bugger all', b'here', b'earth!')


# py -2
import re
S = 'Bugger all down here on earth!'      # 단순 텍스트와 바이너리
U = u'Bugger all down here on earth!'     # 유니코드 텍스트

re.match('(.*) down (.*) on (.*)', S).groups()
# ('Bugger all', 'here', 'earth!')

re.match('(.*) down (.*) on (.*)', U).groups()
# (u'Bugger all', u'here', u'earth!')


# py -3
import re
S = 'Bugger all down here on earth!'
B = b'Bugger all down here on earth!'

re.match('(.*) down (.*) on (.*)', B).groups()
# TypeError: cannot use a string pattern on a bytes-like object

re.match(b'(.*) down (.*) on (.*)', S).groups()
# TypeError: cannot use a bytes pattern on a string-like object

re.match(b'(.*) down (.*) on (.*)', bytearray(B)).groups()
# (b'Bugger all', b'here', b'earth!')

re.match('(.*) down (.*) on (.*)', bytearray(B)).groups()
# TypeError: cannot use a string pattern on a bytes-like object
