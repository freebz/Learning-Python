# 불일치 디코딩

file = open(r'C:\Python33\python.exe', 'r')
text = file.read()
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 24: invalid start byte


file = open(r'C:\Python33\python.exe', 'rb')
data = file.read()
data[:20]
# b'\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00>\x00'
