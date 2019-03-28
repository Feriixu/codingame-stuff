import sys

message = input()
message_bin = ""
for i in message:
    binary = bin(ord(i))[2:]
    prefix = "0"*(7-len(binary))
    message_bin+= prefix + binary

print("Message is: ", message, file=sys.stderr)
print("Binary is: ", message_bin, file=sys.stderr)

lastchar = message_bin[0]
print("The first char is: ", lastchar, file=sys.stderr)

currcount = 0
message_converted = ""
for i in message_bin:
    print("Current char is: ", i, file=sys.stderr)
    print("Checking if last: ", lastchar, " and current: ", i, " are the same.", file=sys.stderr)

    if lastchar == i: 
        print("YES", file=sys.stderr)
        currcount += 1
    else:
        print("NO", file=sys.stderr)
        print("Current count:", currcount, file=sys.stderr)
        prefix = ["0 ", "00 "][str(lastchar) == "0"]
        print("Prefix is ", prefix, " because lastchar: ", lastchar, file=sys.stderr)
        addition = prefix + ("0" * currcount) + " "
        message_converted += addition
        print("Added: ", addition, file=sys.stderr)
        currcount = 1

    lastchar = i
    
print("Current count:", currcount, file=sys.stderr)
prefix = ["0 ", "00 "][str(lastchar) == "0"]
print("Prefix is ", prefix, " because lastchar: ", lastchar, file=sys.stderr)
addition = prefix + ("0" * currcount) + " "
message_converted += addition
print("Added: ", addition, file=sys.stderr)

print(message_converted.strip())