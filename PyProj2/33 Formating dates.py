from datetime import datetime
from datetime import date


print(datetime.now())
now = datetime.now()
print(now)

print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d-%B-%Y %H:%M:%S")) # B - August
print(now.strftime("%d-%b-%Y %H:%M:%S")) # b - Aug
print("----------------------------------")
print(date.today().strftime("%d-%m-%Y"))
print(date.today().strftime("%d-%B-%Y"))