import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, h = [int(i) for i in input().split()]
print("Width:", l, "Height:", h, file=sys.stderr)

numeral_lines = []
numerals = []
n1 = []
n2 = []

# Function to convert numeral lines to a 2D list for easier comparison
def conv_numeral_lines_to_2D(lines):
    converted = []
    for i in range(0, 20*l, l):
        numeral = []
        for line in lines:
            numeral.append(line[i:i+l])
            
        converted.append(numeral)
        print("Added a numeral", numeral, file=sys.stderr)
    return converted

# Function to convert mayan number into 2D list for easier comparison
def conv_maya_to_2D(mayan_lines):
    converted = []
    for i in range(0, len(mayan_lines), h): # Step through line with step of the height of a digit
        mayan_digit = []
        for j in range(h): # Step through the lines of a single digit and add them to the array
            mayan_digit.append(mayan_lines[i+j])

        converted.append(mayan_digit) # Add the lines to the converted array
        print("Added a digit", mayan_digit, file=sys.stderr)
    return converted

def conv_maya_digits(digit_2D_array, numerals_2D_array):
    values = []
    for digit in digit_2D_array:
        print("What number is", digit, file=sys.stderr)
        for numeral_indx in range(len(numerals_2D_array)):
            numeral = numerals_2D_array[numeral_indx]
            if digit == numeral: 
                values.append(numeral_indx)
                print("Found", numeral_indx, file=sys.stderr)
    return values

def conv_digit_decimal(digits):
    total = 0
    expo = len(digits)
    for i in range(len(digits)):
        expo -= 1
        total += digits[i]*20**expo
    return total

def __DecimalToAnyBaseArrayRecur__(array, decimal, base):
    array.append(decimal % base)
    div = decimal // base
    if(div == 0):
        return
    __DecimalToAnyBaseArrayRecur__(array, div, base)

def DecimalToAnyBaseArray(decimal, base):
    array = []
    __DecimalToAnyBaseArrayRecur__(array, decimal, base)
    return array[::-1]

for i in range(h): # Read the numerals
    numeral_line = input()
    numeral_lines.append(numeral_line)
    print(numeral_line, file=sys.stderr)

# Convert the numeral lines into 2D array
numerals = conv_numeral_lines_to_2D(numeral_lines)

print("Reading Number 1", file=sys.stderr)
s1 = int(input())
for i in range(s1): # Read number 1
    num_1line = input()
    n1.append(num_1line)
    # print(num_1line, file=sys.stderr)

print("Reading Number 2", file=sys.stderr)
s2 = int(input())
for i in range(s2): # Read number 2
    num_2line = input()
    n2.append(num_2line)
    # print(num_2line, file=sys.stderr)

operation = input() # Read the operation
print("Operation is", operation, file=sys.stderr)

number1_converted = conv_maya_digits(conv_maya_to_2D(n1), numerals)
number2_converted = conv_maya_digits(conv_maya_to_2D(n2), numerals)
print(number1_converted, file=sys.stderr)
print(number2_converted, file=sys.stderr)

decimal1 = conv_digit_decimal(number1_converted)
decimal2 = conv_digit_decimal(number2_converted)

print(decimal1, decimal2, file=sys.stderr)

decimal_answer = int(eval(str(decimal1) + operation + str(decimal2)))
print("Decimal Answer is", decimal_answer, file=sys.stderr)

answer_base20 = DecimalToAnyBaseArray(decimal_answer, 20)

print(answer_base20, file=sys.stderr)

for digit in answer_base20:
    for numeral_line in numerals[digit]:
        print(numeral_line)
