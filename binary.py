int_num = int(input("input your number: "))
original_num = int_num  # Save the original number so we can print it later!
binary_str = ""

if int_num == 0:
    print("Your number is 0 as you inputed -0-")
    binary_str = "0"
else:
    while int_num > 0:
        binary_num = int_num % 2
        binary_str = str(binary_num) + binary_str  # Use binary_num (the remainder) here!
        int_num = int_num // 2

print(f"binary form of your inputted number {original_num} is {binary_str}")