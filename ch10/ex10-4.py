# 사용자 입력으로 연산하기

reply = '20'
reply ** 2
# ...에러 텍스트 생략...
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'


int(reply) ** 2
# 400


while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    print(int(reply) ** 2)
print('Bye')
