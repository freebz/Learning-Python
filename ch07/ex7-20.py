# 키, 속성, 오프셋 추가하기

import sys

'My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})
# 'My laptop runs win32'
'My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'})
# 'My laptop runs win32'


somelist = list('SPAM')
somelist
# ['S', 'P', 'A', 'M']

'first={0[0]}, third={0[2]}'.format(somelist)
# 'first=S, third=A'

'first={0}, last={1}'.format(somelist[0], somelist[-1]) # 포맷에서 [-1]은 실패
# 'first=S, last=M'

parts = somelist[0], somelist[-1], somelist[1:3] # 포맷에서 [1:3]은 실패
'first={0}, last={1}, middle={2}'.format(*parts) # 또는 2.&/3.1+에서 {} 사용
# "first=S, last=M, middle=['P', 'A']"
