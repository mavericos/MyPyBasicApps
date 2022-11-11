

try:
    number = int(input("Enter a number "))
    print(number)
except ZeroDivisionError as err: #най-добра практика в Python
    print(err)
except ValueError:
    print("invalid input")

#Така ако след първия принт има ерор, ще изведе втория принт