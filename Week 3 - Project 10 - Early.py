hourlyPay = float(input("Enter your hourly wage:"))

hoursWorked = float(input("Enter your hours worked:"))

overtimeHours = float(input("Enter your overtime hours worked: "))

regularPay = hourlyPay * hoursWorked

overtimePay = overtimeHours * (hourlyPay * 1.5)

weeklyPay = overtimePay + regularPay

print("For the week you have made", weeklyPay)
