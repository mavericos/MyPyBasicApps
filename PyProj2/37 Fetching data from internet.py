from urllib import request

r = request.urlopen("http://www.google.com")

print(r)
print(r.getcode())
print(r.read())



