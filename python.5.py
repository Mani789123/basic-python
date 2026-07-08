n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Employee Name: ")
    basic = float(input("Basic Salary: "))

    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da

    if gross > 50000:
        tax = gross * 0.10
    else:
        tax = gross * 0.05

    net = gross - tax

    print("\nEmployee:", name)
    print("Gross Salary:", gross)
    print("Tax:", tax)
    print("Net Salary:", net)