# 이스케이프 시퀀스는 특수문자를 표현

s = 'a\nb\tc'
s
# 'a\nb\tc'
print(s)
# a
# b	c


len(s)
# 5


s = 'a\0b\0c'
s
# 'a\x00b\x00c'
len(s)
# 5



s = '\001\002\x03'
s
# '\x01\x02\x03'
len(s)
# 3


S = "s\tp\na\x00m"
S
# 's\tp\na\x00m'
len(S)
# 7
print(S)
# s	p
# a m


x = "C:\py\code"                # \ 리터럴을 유지하며 \\처럼 출력
x
# 'C:\\py\\code'
len(x)
# 10
