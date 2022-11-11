person = {
    "name" : "Ivan",
    "age" : 20,
    "adress" : "Bulgaria"
    #key    :   value
}
for key, value in person.items():
    print(f"key: {key} value:{value}")

for key in person:
    print(f"key: {key} value:{person[key]}")

#същият резултат по друг начин

print(person.items())