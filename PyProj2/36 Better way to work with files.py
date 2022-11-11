import os.path

filename = "./date.csv"
# проверява името, ако е друго ще изведе else

if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())

else:
    print(f"file {filename} does not exist")
