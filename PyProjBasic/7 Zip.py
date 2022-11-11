# Zip

names = ['Tim', 'Ben', 'Jim', 'Boe', 'Dan']
ages = [21, 19, 18, 42, 65, 14, 3]
eye_color = ['blue', 'brown', 'red', 'green', ]

print(list(zip(names, ages, eye_color)))

print(list(zip(names, eye_color)))

for name, age, eye_color in zip(names, ages, eye_color):
    if age > 20:
        print(name)
    print(eye_color)

