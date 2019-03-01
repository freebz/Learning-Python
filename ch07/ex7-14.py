# 다른 문자열 메서드

line = "The knights who say Ni!\n"
line.rstrip()
# 'The knights who say Ni!'
line.upper()
# 'THE KNIGHTS WHO SAY NI!\n'
line.isalpha()
# False
line.endswith('Ni!\n')
# True
line.startswith('The')
# True


line
# 'The knights who say Ni!\n'

line.find('Ni') != -1           # 메서드 호출이나 표현식을 통한 검색
# True
'Ni' in line
# True

sub = 'Ni!\n'
line.endswith(sub)              # 메서드 호출 또는 슬라이스를 통한 문자열 끝 테스트
# True
line[-len(sub):] == sub
# True
