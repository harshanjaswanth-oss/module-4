


num = int(input("Enter a number: "))


if num == 0:
    print("Binary: 0")
else:
    binary_digits = []

  
    while num > 0:
        remainder = num % 2
        binary_digits.append(remainder)
        num //= 2

    
    binary_str = ""
    for i in range(len(binary_digits) - 1, -1, -1):
        binary_str += str(binary_digits[i])

    print("Binary:", binary_str)
