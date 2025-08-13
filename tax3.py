import tax1
if tax1.Gross_monthly_Salary >= 0 and tax1.Gross_monthly_Salary < 30_0000:
    print("The tax is 0% ")
elif tax1.Gross_monthly_Salary >= 30_0001 and tax1.Gross_monthly_Salary < 60_0000:
    print("The tax is 5% ")
elif tax1.Gross_monthly_Salary >= 600001 and tax1.Gross_monthly_Salary < 900000:
    print("The tax is 10% ")
elif tax1.Gross_monthly_Salary >= 900001 and tax1.Gross_monthly_Salary < 1200000:
    print("The tax is 15% ")
elif tax1.Gross_monthly_Salary >= 1200001 and tax1.Gross_monthly_Salary < 1500000:
    print("The tax is 20% ")
else:
    tax1.Gross_monthly_Salary >= 1500000
    print("The tax is 30% ")

    



