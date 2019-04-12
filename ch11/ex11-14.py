# 파이썬 3.X print 함수

# c:\python36\python
print()                         # 빈 라인 출력

x = 'spam'
y = 99
z = ['eggs']

print(x, y, z)                  # 기본 옵션으로 세 개의 객체 출력
# spam 99 ['eggs']


print(x, y, z, sep='')          # 구분자 제거
# spam99['eggs']

print(x, y, z, sep=', ')        # 사용자 정의 구분자
# spam, 99, ['eggs']


print(x, y, z, end='')          # 라인 종료 방지
# spam 99 ['eggs']>>>

print(x, y, z, end=''); print(x, y, z) # 같은 출력 라인에 두 개의 출력
# spam 99 ['eggs']spam 99 ['eggs']
print(x, y, z, end='...\n')     # 사용자 정의 라인 종료
# spam 99 ['eggs']...


print(x, y, z, sep='...', end='!\n') # 다수의 키워드
# spam...99...['eggs']!
print(x, y, z, end='!\n', sep='...') # 순서는 중요하지 않음
# spam...99...['eggs']!


print(x, y, z, sep='...', file=open('data.txt', 'w')) # 파일에 출력
print(x, y, z)                                        # 다시 표준 출력
# spam 99 ['eggs']
print(open('data.txt').read())                        # 파일 텍스트 표시
# spam 99 ['eggs']


text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
print(text)
# Result: 3.1416, 00042
print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))
# Result: 3.1416, 00042
