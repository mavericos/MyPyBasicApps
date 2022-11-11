number = 10
message = "positive" if number > 0 else "0 or negative"
print(message)  # по-сбит вариант, приложим при само един If

if number > 0:
    print("positive")
else:
    print("0 or negative")

    #при повече elif , тоьи начин е удачен