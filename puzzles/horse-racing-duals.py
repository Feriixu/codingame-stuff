import sys
import math


n = int(input())
horses = []
for i in range(n):
    horses.append(int(input()))

def slow_approach(horses):
    mindiff = math.inf
    for i_horse in range(len(horses)):
        for i_horse2 in range(i_horse+1, len(horses), 1):
            diff = abs(horses[i_horse] - horses[i_horse2])
            if diff < mindiff:
                mindiff = diff
    return mindiff

def fast_approach(horses):
    horses.sort()
    mindiff = math.inf
    for i in range(len(horses)-1):
        diff = horses[i+1] - horses[i]
        if diff < mindiff:
            mindiff = diff
    return mindiff

print(fast_approach(horses))


