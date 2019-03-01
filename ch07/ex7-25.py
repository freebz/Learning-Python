# 유연한 참조 구문: 추가적인 복잡성과 기능의 중복

'{name} {job} {name}'.format(name='Bob', job='dev')
# 'Bob dev Bob'
'%(name)s %(job)s %(name)s' % dict(name='Bob', job='dev')
# 'Bob dev Bob'


D = dict(name='Bob', job='dev')
'{0[name]} {0[job]} {0[name]}'.format(D) # 메서드 키 참고
# 'Bob dev Bob'
'{name} {job} {name}'.format(**D) # 메서드, 딕셔너리를 인수로 풀어냄
# 'Bob dev Bob'
'%(name)s %(job)s %(name)s' % D # 표현식, 키 참고
# 'Bob dev Bob'
