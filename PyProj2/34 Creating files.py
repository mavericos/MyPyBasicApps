file = open("./date.csv", "r+")
# може Writing , Appending, Reading, R+eading/writing
file.write("id, name, email\n")
file.write("1, Jameson, Jameson@drink.com\n")
file.write("2, Bushmils, Bush@drink.com\n")
file.close()