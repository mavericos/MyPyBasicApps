class MyClass:

    def __init__(self):
        self.value=132
        print("Създаване на обект:", self.value)
    def __del__(self):
        print("Изтрива се обект:", self.value)
    def set(self,n):
        self.value=n
    def show(self):
        print("Поле на обекта: ",self.value)

obj=MyClass()
obj.show()
obj.set(100)
MyClass.show(obj)
MyClass.set(obj,200)
obj.show()
MyClass.__init__(obj)
MyClass.__del__(obj)
obj.show()
obj.value=321
obj.show()
obj.__init__()
obj.__del__()
obj.show()