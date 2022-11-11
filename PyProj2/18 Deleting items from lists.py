numbers = [1, 2, 3, 4, -1, -20]
print(numbers)

numbers.remove(2)
print(numbers)

numbers.pop()
print(numbers)

numbers.pop()   #маха последното число в листа -20
print(numbers)

del numbers[0]  #трие числото с идекс 0
print(numbers)

nom = [55, 23, 65, 789, 432]
print(nom)
del nom[4]  #трие числоро а индекс 4
print(nom)
nom.sort()
print(nom)

del nom [0:3] #трие индексите от 0 до 3
print(nom)