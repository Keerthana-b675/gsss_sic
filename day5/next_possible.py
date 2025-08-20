def next_bigger_number(n):
    digits = list(str(n))
    length = len(digits)

    # Step 1: Find the rightmost digit that is smaller than the digit next to it
    for i in range(length - 2, -1, -1):  #goes and checks the compare of 2 elements
        if digits[i] < digits[i + 1]:
            break
    else:
        return "No higher permutation possible"

    # Step 2: Find the smallest digit on the right side of (i) which is bigger than digits[i]
    for j in range(length - 1, i, -1):
        if digits[j] > digits[i]:
            break

    # Step 3: Swap digits[i] and digits[j]
    digits[i], digits[j] = digits[j], digits[i]

    # Step 4: Reverse the digits after position i
    digits[i + 1:] = reversed(digits[i + 1:])

    # Convert back to integer
    return int(''.join(digits))


# Example usage
number = int(input("Enter a number: "))
result = next_bigger_number(number)
print("Next bigger number:", result)
