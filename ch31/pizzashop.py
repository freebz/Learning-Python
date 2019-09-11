# -*- coding: utf-8 -*-
# pizzashop.py(2.X+3.X) 파일
from __future__ import print_function
from employees import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "orders from", server)
    def pay(self, server):
        print(self.name, "pays for item to", server)

class Oven:
    def bake(self):
        print("oven bakes")

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')      # 다른 객체를 내포시킴
        self.chef = PizzaRobot('Bob')    # bob이라는 이름의 로봇
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name)        # 다른 객체를 활성화
        customer.order(self.server)      # 서빙직원으로부터 고객 주문을 받음
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop()                  # 복합 객체 생성
    scene.order('Homer')                 # Homer의 주문을 시뮬레이션
    print('...')
    scene.order('Shaggy')                # Shaggy의 주문을 시뮬레이션
