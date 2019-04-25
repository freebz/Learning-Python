# 확장 리스트 컴프리헨션 구문

# 필터절: if

lines = [line.rstrip() for line in open('script2.py') if line[0] == 'p']
lines
# ['print(sys.path)', 'print(x ** 32)']


res = []
for line in open('script2.py'):
    if line[0] == 'p':
        res.append(line.rstrip())

res
# ['print(sys.path)', 'print(x ** 32)']


[line.rstrip() for line in open('script2.py') if line.rstrip()[-1].isdigit()]
# ['x = 2']


fname = r'd:\books\5e\lp5e\draft1typos.txt'                  # 전체 라인
len(open(fname).readlines())
# 263
len([line for line in open(fname) if line.strip() != ''])    # 빈 라인 제외
# 185
