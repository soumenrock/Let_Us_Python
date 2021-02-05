"""Calculate gross salary if DA=40% of basic, HRA=20% of basic"""

basic = int(input("Enter basic salary: "))
da = (40 * basic)/100
hra = (20 * basic)/100
print("DA = ", int(da))
print("HRA = ", int(hra))
print("Gross Salary = Basic + DA + HRA = ", int(basic + da + hra))