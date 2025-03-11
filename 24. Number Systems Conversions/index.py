# convert decimal to binary,octal,hexadecimal

decimal = eval(input("Enter a number in base 10: "))

print(f"Base 2 form i.e binary form of {decimal} is: {str(bin(decimal))[2:]}")          ## "str(bin(decimal))[2:]" --> bin(dec) se 0b remove because ans ka form is "0bXXXX"
print(f"Base 8 form i.e octal form of {decimal} is: {str(oct(decimal))[2:]}")          ## "str(oct(decimal))[2:]" --> bin(dec) se 0b remove because ans ka form is "0oXXXX"
print(f"Base 16 form i.e hexadecimal form of {decimal} is: {str(hex(decimal))[2:]}")          ## "str(hex(decimal))[2:]" --> bin(dec) se 0b remove because ans ka form is "0xXXXX"