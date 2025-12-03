class Father:
    def car(self):
        print("Father has a car")

class Mother:
    def house(self):
        print("Mother has a house")

class Child(Father, Mother):
    pass

c = Child()
c.car()
c.house()

