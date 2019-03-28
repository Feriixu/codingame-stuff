unc = ""
string = ""
for c in unc:
    string += hex(ord(c))[2:]
print(string)
half = int(len(string)/2)
A = string[:half]
B = string[half:]
print(A, B)

final = ""
for i in range(len(A)):
    final += A[i]
    final += B[i]
    
print(final)

