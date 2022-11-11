employee_file = open("employee.txt", "a")
employee_file.write("\nTobi Papaprchev")
employee_file.write("\nBobo Babchev")
employee_file.close()

test_file = open("test.txt", "w")
test_file.write("Boncho Troshev")
test_file.write("\nGanka Trosheva")
test_file.close()