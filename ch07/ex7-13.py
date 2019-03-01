# 문자열 메서드 예제: 문자열 분석

line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
col1
# 'aaa'
col3
# 'ccc'


line = 'aaa bbb ccc'
cols = line.split()
cols
# ['aaa', 'bbb', 'ccc']


line = 'bob,hacker,40'
line.split(',')
# ['bob', 'hacker', '40']


line = "i'mSPAMaSPAMlumberjack"
line.split("SPAM")
# ["i'm", 'a', 'lumberjack']
