# https://www.youtube.com/watch?v=x5Qoz-l3NYY&list=PLnbmk43t7uQNYIaPU8RoGlMeI6L_WArKB&index=9
# if - Else Statement

age = 17
valid = "You`re an adult"
invalid = "You`re NOT an adult"

if age >= 18:
    print(valid)
else:
    print(invalid)

# better way to write it
print(valid) if age >= 18 else print(invalid)

