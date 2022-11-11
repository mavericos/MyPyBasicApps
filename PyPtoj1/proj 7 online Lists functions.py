lucky_numbers = [49, 88, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "James", "Spas", "Spas", "Spas", "Gosho"]

friends.extend(lucky_numbers) #разширяваме friends с lucky numbers
print(friends)

friends.append("Creed") #Добавя Creed към списъка с friends
print(friends)

friends.insert(1, "Kelly") #добавя Келли на позиция 1 и избутва останалите напред
print(friends)

friends.pop() #Премахва последният елемент от листа
print(friends)
friends.pop() #Премахва последният елемент от листа
print(friends)
friends.pop() #Премахва последният елемент от листа
print(friends)

print(friends.index("Gosho")) #Вади индекса под Гошо
print(friends.index("James"))
print(friends.count("Spas")) #Колко пъти има спас в списъка

friends2 = ["Bobo" , "Jango", "Momo", "Bubu"]
friends2.sort() #сортира по азбучен ред
print(friends2)

lucky_numbers.sort() #сортира числата малко към голямо
print(lucky_numbers)

lucky_numbers.reverse()  #сортира ги от голямо към малко
print(lucky_numbers)

friends7 = friends.copy()  #копира списъка
print(friends7)


friends.clear()
print(friends)