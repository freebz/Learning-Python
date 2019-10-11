# 파일 입력 디코딩

# 파일에서 읽을 때 자동으로 디코드
open('latindata', 'r', encoding='latin-1').read()    # 입력 시 디코드
# 'AÄBèC'
open('utf8data', 'r', encoding='utf-8').read()       # 인코딩 타입에 따름
# 'AÄBèC'

X = open('latindata', 'rb').read()          # 수동 디코딩
X.decode('latin-1')                         # 필요 없음
# 'AÄBèC'

X = open('utf8data', 'rb').read()
X.decode()    # UTF-8 is default
# 'AÄBèC'
