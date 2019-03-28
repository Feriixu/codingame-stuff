import sys
import math

n = int(input())  # the number of temperatures to analyse

temps = []
if n !=0:
    for i in input().split(): temps.append(int(i))
    temps.sort(reverse=True)
    closest = min(temps, key=abs)
    print("Out of ", temps, file=sys.stderr)
    print(closest)
    print("is the closest to zero.", file=sys.stderr)

else:
    print("No Temperatures were given", file=sys.stderr)
    print("0")