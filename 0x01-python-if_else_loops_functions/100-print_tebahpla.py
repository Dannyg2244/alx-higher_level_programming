#!/usr/bin/python3
for i in range(122, 64, -1):
    print(chr(i), end="")
    if i % 2 == 0:
        i -= 32
    else:
        i += 32
