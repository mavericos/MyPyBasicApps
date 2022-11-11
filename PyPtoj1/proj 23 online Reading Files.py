employee_file = open("test.txt", "r")
# "r" - read only   "w" - write променя инф.
print(employee_file.readable())  #True , readable е "r"
print(employee_file.writable())  #False, горе е "r" , само readable

print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)
employee_file.close()

