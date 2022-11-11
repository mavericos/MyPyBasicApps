# For Else & While Else

search = [1, 2, 3, 4, 5, 6, 7]
target = 7
found = False
for element in search:
    if element == target:
        print('I found it!')
        break
else:
    print("I didn`t find it")