
# Read in files with different actions - read, write, append, read+
employee_file = open("../venv/data/employees.txt", "w")


employee_file.write("Gymbob - manager\n")

employee_file.close()