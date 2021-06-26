#!/bin/python3
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem

import math
import os
import random
import re
import sys

def recursion(string):
    if (len(str(string))==1):
        return string
    else:
        string = sum(int(p) for p in str(string))
        return (recursion(string))

# Complete the superDigit function below.
def superDigit(n, k):
    initialSum = sum(int(p) for p in str(n)) * k 
    return (recursion(initialSum))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    #fptr.write(str(result) + '\n')

    #fptr.close()