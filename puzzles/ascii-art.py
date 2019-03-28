import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

width = int(input())
height = int(input())
text = input()
asciirows = []
for i in range(height):
    asciirow = input()
    print("Asciirow is: ", asciirow, file=sys.stderr)
    textrow = ""
    for letter in text:
        print("Handling letter: ", letter, file=sys.stderr)
        if not (letter.isalpha()): 
            print("Letter is not Alpha", file=sys.stderr)
            textrow += asciirow[width * 26 :]
        else:
            position = ord(letter.upper()) - 65
            ascii_representation = asciirow[width * position:width * position + width]
            textrow += ascii_representation
    asciirows.append(textrow)


for line in asciirows:
    print(line)
