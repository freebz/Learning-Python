# 더 생각해 볼 주제: 딕셔너리 인터페이스

import dbm                      # 파이썬 2.X에서는 anydbm으로 사용
file = dbm.open("filename")     # 파일 연결
file['key'] = 'data'            # 키에 의해 데이터 저장
data = file['key']              # 키에 의해 데이터 가져오기


import cgi
form = cgi.FieldStorage()       # 폼(form) 데이터 분석
if 'name' in form:
    showReply('Hello, ' + form['name'].value)
