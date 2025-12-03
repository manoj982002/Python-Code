class Student:
    def __init__(self):
        self.name = "manoj"
        self._age = 22
        self.__marks = 88
    def get__marks(self):
        return self.__marks

s = Student()
print(s.name)
print(s._age)
print(s.get__marks())