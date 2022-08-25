#!/usr/bin/python3
for alphabets in range(ord('a'), ord('z')+1):
     if (alphabets != 101 and alphabets != 113):
         print('{:c}'.format(alphabets), end='')
