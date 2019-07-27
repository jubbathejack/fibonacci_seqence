#!/usr/bin/env python3

x = 0
y = 1
seqNum = 3

rangeTop = input("Please enter how many iterations you want to run: ")
rangeTop = int(rangeTop)

print("1: " + str(x))
print("2: " + str(y))

while seqNum <= rangeTop:
    x = (x + y)
    print(str(seqNum) + ": " + str(x))
    seqNum = (seqNum + 1)
    if seqNum > rangeTop:
        print("Fibonacci sequence complete.")
        exit(0)
    else:
        pass
    y = (y + x)
    print(str(seqNum) + ": " + str(y))
    seqNum = (seqNum + 1)
else:
    print("Fibonacci sequence complete.")

