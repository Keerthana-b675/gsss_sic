def next_bigger_number(n):
    digits = list(str(n))
    length = len(digits)

    for i in range (length ):
        if digits[i] < digits[i + 1]:
            break
        else:
            return -1
    for j in range(0,9999):
        if digits[j] > digits[i]:
            break
    digits[i], digits[j] = digits[j], digits[i]
    return int(''.join(digits))
number = int(input("Enter a number: "))
result = next_bigger_number(number)
print("Next bigger number:", result)
        