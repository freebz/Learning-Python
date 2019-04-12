# 버전 중립적인 출력

# 2to3 변환기

# from __future__ 임포트

from __future__ import print_function


# 코드를 이용하여 출력 차이 없애기

# c:\python36\python
print('spam')                   # 3.X print 함수 호출 구문
# spam
print('spam', 'ham', 'eggs')    # 다수의 인수 사용
# spam ham eggs


# c:\python27\python
print('spam')                   # 괄호로 감싼 2.X print문
# spam
print('spam', 'ham', 'eggs')    # 이 결과는 셀제 튜플 객체다!
# ('spam', 'ham', 'eggs')


# py -2
print()                         # 이 코드는 3.X에서 개행 문자를 의미함
# ()
print('')                       # 이 코드는 2.X와 3.X 모두에서 개행 문자를 의미함


print('%s %s %s' % ('spam', 'ham', 'eggs'))
# spam ham eggs
print('{0} {1} {2}'.format('spam', 'ham', 'eggs'))
# spam ham eggs
print('answer: ' + str(42))
# answer: 42
