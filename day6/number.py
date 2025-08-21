def numbers(num):
    while True:
     digit=str(num)
     ascending_order = int("".join(sorted(digit)))
     descending_order = int("".join(sorted(digit, reverse=True)))
     new_num = descending_order - ascending_order
     print(f"{descending_order} - {ascending_order} = {new_num}")

     if new_num == num:   
        break
     num = new_num
    
    print("Final digit is:", num)

n = int(input("Enter a 4-digit number: "))
numbers(n)
