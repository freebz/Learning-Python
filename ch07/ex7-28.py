# 함수 vs 표현식: 사소한 편의

def myformat(fmt, args): return fmt % args # 파트 4 참조

myformat('%s %s', (88, 99))     # 직접 만든 함수 객체 호출
str.format('{} {}', 88, 99)     # 그리고 내장된 함수 호출

otherfunction(myformat)         # 직접 만든 함수 또한 객체


'%(num)i = %(title)s' % dict(num=7, title='Strings')
# '7 = Strings'
'{num:d} = {title:s}'.format(num=7, title='Strings')
# '7 = Strings'
'{num} = {title}'.format(**dict(num=7, title='Strings'))
# '7 = Strings'


import string
t = string.Template('$num = $title')
t.substitute({'num': 7, 'title': 'Strings'})
# '7 = Strings'
t.substitute(num=7, title='Strings')
# '7 = Strings'
t.substitute(dict(num=7, title='Strings'))
# '7 = Strings'
