class GrandFather:
    def house(self):
        print("Grandfather's house")

class Father(GrandFather):
    def car(self):
        print("Father's car")

class Son(Father):
    def bike(self):
        print("Son's bike")

s = Son()
s.house()
s.car()
s.bike()
