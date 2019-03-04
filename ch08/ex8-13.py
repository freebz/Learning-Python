# 미리 보기: 값을 키에 연결하기

table = {'Holy Grail': '1975',  # 키 => 값(제목 => 연도)
         'Life of Brian': '1979',
         'The Meaning of Life': '1983'}

table['Holy Grail']
# '1975'

list(table.items())             # 값 => 키(연도 => 제목)
# [('Holy Grail', '1975'), ('Life of Brian', '1979'), ('The Meaning of Life', '1983')]
[title for (title, year) in table.items() if year == '1975']
# ['Holy Grail']


K = 'Holy Grail'
table[K]                        # 키 => 값(일반적인 사용법)
# '1975'

V = '1975'
[key for (key, value) in table.items() if value == V]    # 값 => 키
# ['Holy Grail']
[key for key in table.keys() if table[key] == V]         # 위와 같다
# ['Holy Grail']
