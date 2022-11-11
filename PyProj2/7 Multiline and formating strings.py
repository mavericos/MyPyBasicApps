import random
name = "Ivan"
age = 55
email = """Zdravei {}, 
Kak si?
Beshe mi priqtno da pogovorim
"""
print(email)
print(email.format(name))
# Форматира name на мястото на {}

email2 = f"""Zdrawei {name},
Kakvo pravish?
Qdesh li meso?
Godinite ti sa {age + 9}
"""
# Поставям f в началото и директно въвеждам name в {}
print(email2)
