# 예제: 영화 데이터베이스

table = {'1975': 'Holy Grail',  # 키: 값
         '1979': 'Life of Brian',
         '1983': 'The Meaning of Life'}

year = '1983'
movie = table[year]             # 딕셔너리[키] => 값
movie
# 'The Meaning of Life'
for year in table:              # 다음과 같음. for year in table.keys()
    print(year + '\t' + table[year])

# 1975	Holy Grail
# 1979	Life of Brian
# 1983	The Meaning of Life
