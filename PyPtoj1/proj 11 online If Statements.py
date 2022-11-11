is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):  #отрицанието трябва да е в ()
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are are not male but are tall")
else:
    print("You are either not male or not tall")

