# 파일명: 텍스트 vs 바이트

f = open('xxx\u00A5', 'w')      # 아스키가 아닌 파일명
f.write('\xA5999\n')            # 다섯 문자를 기록
f.close()
print(open('xxx\u00A5').read()) # 텍스트: 자동 인코드됨
# ¥999
print(open(b'xxx\xA5').read())  # 바이트: 미리 인코드됨
# ¥999

import glob                     # 파일명 확장 도구
glob.glob('*\u00A5*')           # 디코드된 텍스트: 디코드된 텍스트 반환
# ['xxx¥']
glob.glob(b'*\xA5*')            # 인코드된 바이트: 인코드된 바이트 반환
# [b'xxx\xa5']
