# 실제에서의 다형성

if __name__ == '__main__':
    ...
    print('--All three--')
    for obj in (bob, sue, tom):    # 객체를 일반적으로 처리함
        obj.giveRaise(.10)         # 이 객체의 giveRaise를 실행
        print(obj)                 # 보편적인 __repr__을 실행


# [Person: Bob Smith, 0]
# [Person: Sue Jones, 100000]
# Smith Jones
# [Person: Sue Jones, 110000]
# Jones
# [Person: Tom Jones, 60000]
# --All three--
# [Person: Bob Smith, 0]
# [Person: Sue Jones, 121000]
# [Person: Tom Jones, 72000]
