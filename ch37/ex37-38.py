# 더 생각해 볼 주제: 파일 검사하기와 파일 이외의 수많은 것들

f = open('py33-windows-launcher.html', encoding='utf8')
t = f.read()
for (i, c) in enumerate(t):
    try:
        x = c.encode(encoding='ascii')
    except:
        print(i, sys.exc_info()[0])
# 9886 <class 'UnicodeEncodeError'>


len(t)
# 31021
t[9800:9890]
# 'ugh.  \u206cThi'
t[9870:9080]
# 'trace through.  \u206cThi'


f = open('py33-windows-launcher.html', 'rb')
b = f.read()
b[0]
# 60
b[:10]
# b'<HTML>\r\n<T'
