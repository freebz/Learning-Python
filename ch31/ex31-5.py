# 더 생각해 볼 주제: 클래스와 지속성

import pickle
object = SomeClass()
file   = open(filename, 'wb')   # 외부 파일 생성
pickle.dump(object, file)       # 파일에 객체 저장

import pickle
file   = open(filename, 'rb')
object = pickle.load(file)      # 나중에 이를 다시 가져옴


import shelve
object = SomClass()
dbase  = shelve.open(filename)
dbase['key'] = object           # key 아래 저장

import shelve
dbase  = shelve.open(filename)
object = dbase['key']           # 나중에 이를 되불러 옴


from pizzashop import PizzaShop
shop = PizzaShop()
shop.server, shop.chef
# (<Employee: name=Pat, salary=40000>, <Employee: name=Bob, salary=50000>)
import pickle
pickle.dump(shop, open('shopfile.pkl', 'wb'))


import pickle
obj = pickle.load(open('shopfile.pkl', 'rb'))
obj.server, obj.chef
# (<Employee: name=Pat, salary=40000>, <Employee: name=Bob, salary=50000>)

obj.order('LSP')
# LSP orders from <Employee: name=Pat, salary=40000>
# Bob makes pizza
# oven bakes
# LSP pays for item to <Employee: name=Pat, salary=40000>
