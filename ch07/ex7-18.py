# 딕셔너리 기반 포매팅 표현식

'%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'}
# '1 more spam'


                                # 대체 대상을 이용한 템플릿
reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name': 'Bob', 'age': 40} # 대체 값 생성
print(reply % values)               # 대체 수행

# Greetings...
# Hello Bob!
# Your age is 40


food = 'spam'
qty = 10
vars()
# {'food': 'spam', 'qty': 10, ...추가로 파이썬이 설정한 내장된 이름들...}


'%(qty)d more %(food)s' % vars() # 변수 이름이 vars()의 키
# '10 more spam'
