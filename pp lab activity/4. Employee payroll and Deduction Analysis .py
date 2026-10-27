
# Employee Payroll and Deduction Analysis

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

# Calculate gross salary
gross = basic + allowances + overtime + incentives

# Progressive deduction calculation
if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 50000:
    deduction = (20000 * 0.05) + ((gross - 20000) * 0.10)
else:
    deduction = (20000 * 0.05) + (30000 * 0.10) \
                + ((gross - 50000) * 0.15)

# Calculate net salary
net_salary = gross - deduction

# Display salary statement
print("\n======= SALARY STATEMENT =======")
print("Employee Name :", name)
print("--------------------------------")
print(f"Basic Salary  : Rs. {basic:.2f}")
print(f"Allowances    : Rs. {allowances:.2f}")
print(f"Overtime Pay  : Rs. {overtime:.2f}")
print(f"Incentives    : Rs. {incentives:.2f}")
print("--------------------------------")
print(f"Gross Salary  : Rs. {gross:.2f}")
print(f"Total Deduction: Rs. {deduction:.2f}")
print("--------------------------------")
print(f"Net Salary    : Rs. {net_salary:.2f}")
print("================================")
