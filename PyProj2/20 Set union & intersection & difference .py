lettersA = {"A", "B", "C", "D"}
lettersB = {"A", "D", "E", "F"}

print(lettersA | lettersB)
# =
union = lettersA | lettersB
# С | изважда всички, без повтарящите се
intersection = lettersA & lettersB
# С & се извежда само повтарящите се

print(union)
print(intersection)

difference = lettersB - lettersA
#извежда само неповтарящите се

print(f"Union = {union}")
print(f"Intersection = {intersection}")
print(f"Difference = {difference}")