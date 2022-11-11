person = {
    "name": "Jamal",
    "age" : 44,
    "adress" : "Pakistan"
    #key        #values
    #keys have to be unique
}
print(person["name"])
print(person["age"])
print(person["adress"])

print(person.keys())
print(person.values())

person["age"] = 100  #модифцира age
print(person)