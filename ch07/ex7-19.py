# 문자열 포매팅 메서드 호출

# 포매팅 메서드 기본

template = '{0}, {1} and {2}'   # 위치
template.format('spam', 'ham', 'eggs')
# 'spam, ham and eggs'

template = '{motto}, {pork} and {food}' # 키워드
template.format(motto='spam', pork='ham', food='eggs')
# 'spam, ham and eggs'

template = '{motto}, {0} and {food}' # 둘 모두
template.format('ham', motto='spam', food='eggs')
# 'spam, ham and eggs'

template = '{}, {} and {}'      # 상대적인 위치
template.format('spam', 'ham', 'eggs') # 2.7과 3.1에 추가
# 'spam, ham and eggs'


template = '%s, %s and %s'      # 표현식을 이용한 방법
template % ('spam', 'ham', 'eggs')
# 'spam, ham and eggs'

template = '%(motto)s, %(pork)s and %(food)s'
template % dict(motto='spam', pork='ham', food='eggs')
# 'spam, ham and eggs'


'{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
# '3.14, 42 and [1, 2]'


X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
X
# '3.14, 42 and [1, 2]'

X.split(' and ')
# ['3.14, 42', '[1, 2]']

Y = X.replace('and', 'but under no circumstances')
Y
# '3.14, 42 but under no circumstances [1, 2]'
