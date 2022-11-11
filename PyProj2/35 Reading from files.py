# може Writing , Appending, Reading, R+eading/writing
file = open("./date.csv", "r")

# print(file.read())   # четене на файла

for line in file:
   print(line)

# print(file.readlines())
file.close()