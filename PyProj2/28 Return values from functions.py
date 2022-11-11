def is_adult(age):
    return age >= 16
def convertGender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"Gender {gender} is unknown"

result = is_adult(19)
print(result)

print(convertGender("F"))
print(convertGender("f"))
print(convertGender("M"))
print(convertGender("m"))
print(convertGender("hello"))