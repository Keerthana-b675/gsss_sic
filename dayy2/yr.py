year=int(input("enter the year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This year is a Leap Year")
        else:
            print("This year is not a Leap Year")
    else:
        print("This year is a Leap Year ")
else:
    print("This year is not a Leap Year")
