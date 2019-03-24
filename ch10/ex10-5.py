# 입력 테스트를 통한 에러 처리하기

S = '123'
T = 'xxx'
S.isdigit(), T.isdigit()
# (True, False)


while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')
