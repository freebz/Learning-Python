# % 포매팅 표현식과 비교

print('%s=%s' % ('spam', 42))   # 포맷 표현식: 2.X/3.X 모두에서 동작

print('{0}={1}'.format('spam', 42)) # 포맷 메서드:3.0+와 2.6+

print('{}={}'.format('spam', 42)) # 자동 숫자 매기기: 3.1+과 2.7



'%s, %s and %s' % (3.14, 42, [1, 2]) # 임의 타입들
# '3.14, 42 and [1, 2]'

'My %(kind)s runs %(platform)s' % {'kind': 'laptop', 'platform': sys.platform}
# 'My laptop runs win32'

'My %(kind)s runs %(platform)s' % dict(kind='laptop', platform=sys.platform)
# 'My laptop runs win32'

somelist = list('SPAM')
parts = somelist[0], somelist[-1], somelist[1:3]
'first=%s, last=%s, middle=%s' % parts
# "first=S, last=M, middle=['P', 'A']"


# 구체적인 포매팅 추가

'%-10s = %10s' % ('spam', 123.4567)
# 'spam       =   123.4567'

'%10s = %-10s' % ('spam', 123.4567)
# '      spam = 123.4567  '

'%(plat)10s = %(kind)-10s' % dict(plat=sys.platform, kind='laptop')
# '     linux = laptop    '

# 부동 소수점 수

'%e, %.3e, %g' % (3.14159, 3.14159, 3.14159)
# '3.141590e+00, 3.142e+00, 3.14159'

'%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159)
# '3.141590, 3.14, 003.14'

# 16진수와 8진수, 그러나 2진수는 지원되지 않음(앞서 설명한 내용 참고)

'%x, %o' % (255, 255)
# 'ff, 377'


# 두 기법에서 하드코딩된 참조
import sys

'My {1[kind]:<8} runs {0.platform:>8}'.format(sys, {'kind': 'laptop'})
# 'My laptop   runs    win32'

'My %(kind)-8s runs %(plat)8s' % dict(kind='laptop', plat=sys.platform)
# 'My laptop   runs    win32'


# 둘 모두에서 사용할 데이터를 미리 생성
data = dict(platform=sys.platform, kind='laptop')

'My {kind:<8} rusn {platform:>8}'.format(**data)
# 'My laptop   rusn    win32'

'My %(kind)-8s runs %(platform)8s' % data
# 'My laptop   rusn    win32'
