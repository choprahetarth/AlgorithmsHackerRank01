#!/bin/python3
import array
import math
import os
import random
import re
import sys
x = 0
countA=0
countB=0
returnArray = [0,0]
# Complete the compareTriplets function below.

def compareTriplets(a, b):
    global countA,countB
    global returnArray
    for x in range(0,2):
        if (a[x]<b[x]):
            countA+=1
        elif (a[x]>b[x]):
            countB+=1
    returnArray = [countA,countB]
    print(returnArray)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()