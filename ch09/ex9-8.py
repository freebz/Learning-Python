# 네이티브 파이썬 객체를 저장하기: pickle

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
import pickle
pickle.dump(D, F)               # 어떠한 객체도 파일로 저장할 수 있음
F.close()


F = open('datafile.pkl', 'rb')
E = pickle.load(F)              # 파일로부터 객체 읽기
E
# {'a': 1, 'b': 2}


open('datafile.pkl', 'rb').read() # 형식은 달라질 수 있음!
# b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02u.'
