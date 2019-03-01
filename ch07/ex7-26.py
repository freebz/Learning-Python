# 명시적 값 참조: 지금은 옵션이지만 더 이상 사용될 것 같지 않음

'\n%s<Class %s, address %s:\n%s%s%s>\n' % (...) # 표현식

'\n{0}<Class {1}, address: {2}:\n{3}{4}{5}>\n'.format(...) # 메서드


'The {0} side {1} {2}'.format('bright', 'of', 'life') # 파있너 3.X, 2.6+
# 'The bright side of life'

'The {} side {} {}'.format('bright', 'of', 'life') # 파이썬 3.1+, 2.7+
# 'The bright side of life'

'The %s side %s %s' % ('bright', 'of', 'life') # 모든 파이썬
# 'The bright side of life'


'{0:f}, {1:.2f}, {2:05.2f}'.format(3.14159, 3.14159, 3.14159)
# '3.141590, 3.14, 03.14'

'{:f}, {:.2f}, {:06.2f}'.format(3.14159, 3.14159, 3.14159)
# '3.141590, 3.14, 003.14'

'%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159)
# '3.141590, 3.14, 003.14'
