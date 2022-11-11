number = 0

while number < 10:
    if number == 5:
        break
    number += 1
    print(number)

print("second way")

while number < 10:
    number += 1
    if number < 5:
       continue
    print(number)

print("third way")

for n in [1,2,3,4,5,6,7]:
    if n < 5:
        continue
    print(n)

print("fourth way")

for m in [1,2,3,4,5,6,7,8]:
    if m == 5:
        break
    print(m)