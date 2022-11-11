def sayhi():
  print("Hello user")  #този код е част от функцията

print("Top")
sayhi()  #извикваме функцията с кода в нея
print("Bottom")

def bye(name, age):   #въвеждаме променлива name и age във функцията
    print("Bye, bye " + name + ", you are " + age)
bye("Gosho", "33")     #добавяме name и age тук
bye("Spas", "22")

def hi(name, age):   #въвеждаме променлива name и age във функцията
    print("Hi, hi " + name + ", you are " + str(age))
hi("Ivan", 33)     #добавяме name и age тук
hi("Gogo", 22)

