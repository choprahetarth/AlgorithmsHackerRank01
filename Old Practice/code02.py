#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
sumRight = 0
sumLeft = 0

def diagonalDifference(arr,index):
    global sumRight
    global sumLeft
    for x in range(index):
        sumRight = sumRight + arr[x][x]
        sumLeft = sumLeft + arr[x][index-1-x]
        print(sumLeft)
        print(sumRight)
    return abs(sumLeft-sumRight)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)
    fptr.write(str(result) + '\n')

    fptr.close()
