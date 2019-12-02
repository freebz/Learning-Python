#!/usr/bin/python
"""
certificate.py 파일: 파이썬 2.X 및 3.X 스크립트
자체 클래스 수료증을 생성함
텍스트와 HTML 파일로 저장되고 출력되며, 웹 브라우저에서 확일할 수 있음
"""
from __future__ import print_function          # 2.X 호환성
import time, sys, webbrowser

if sys.version_info[0] == 2:                   # 2.X 호환성
    input = raw_input
    import cgi
    htmlescape = cgi.escape
else:
    import html
    htmlescape = html.escape

maxline  = 60                                  # 문단 분리선을 포함하기 위함
browser  = True                                # 웹 브라우저에 출력함
saveto   = 'Certificate.txt'                   # 출력 파일명
template = """
%s

===> 공식 수료증 <===

날짜: %s

이 수료증은 %s가 %s의 방대한 내용을 통과하였으며, 이후 웹 사이트나 데스크톱 GUI, 과학 모델, 그리고
복잡한 기능들이 혼합된 응용 프로그램을 개발하는 방법에 대해 학습할 권리를 얻었음을 증명함.
또한, 그 과정에서 Programming Python 같은 훌륭한 책을 참조할 권리도 가졌음을 증명함

-- 강사 마크 러츠

(주의: 이 책의 내용을 건너뛰며 읽었을 경우 인증이 취소됨)

%s
"""

# 대화형. 셋업
for c in 'Congratulations!'.upper():
    print(c, end=' ')
    sys.stdout.flush()                         # 일부 셸은 입력 대기\n
    time.sleep(0.25)
print()

date = time.asctime()
name = input('Enter your name: ').strip() or 'An unknown reader'
sept = '*' * maxline
book = 'Learning Python 5th Edition'

# 텍스트 파일 버전을 만듦
file = open(saveto, 'w')
text = template % (sept, date, name, book, sept)
print(text, file=file)
file.close()

# HTML 파일 버전을 만듦
htmlto = saveto.replace('.txt', '.html')
file = open(htmlto, 'w')

tags = text.replace(sept, '<hr>')              # HTML 태그 삽입
tags = tags.replace('===>', '<h1 align=center>')
tags = tags.replace('<===', '</h1>')

tags = tags.split('\n')                        # 줄 단위 구분
tags = ['<p>' if line == ''
            else line for line in tags]
tags = ['<i>%s</i>' % htmlescape(line) if line[:1] == '\t'
            else line for line in tags]
tags = '\n'.join(tags)

link = '<i><a href="http://learning-python.com/">Book support site</a></i>\n'
foot = '<table>\n<td><img src="ora-lp.jpg" hspace=5">\n</td>%s</table>\n' % link
tags = '<html><body bgcolor=beige>' + tags + foot + '</body></html>'

print(tags, file=file)
file.close()

# 결과 표시
print('[File: %s]' % saveto, end='')
print('\n' * 2, open(saveto).read())

if browser:
    webbrowser.open(saveto, new=True)
    webbrowser.open(htmlto, new=False)

if sys.platform.startswith('win'):
    input('[Press Enter]')              # 윈도우에서 클릭되었을 경우 창이 열린 채로 유지함
