#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
sumPos = 0
sumNeg = 0
sumZer = 0
z = 0
signMatrix = []
sign = lambda x: x and (1, -1)[x < 0]

def plusMinus(arr):
    global sumPos,sumNeg,sumZer,z,signMatrix
    for z in range(len(arr)):
       signMatrix.append(sign(arr[z]))
    print(signMatrix)
    for c in range(len(signMatrix)):
        if (signMatrix[c]==1):
            sumPos = sumPos+1
        elif(signMatrix[c]==-1):
            sumNeg = sumNeg+1
        elif(signMatrix[c]==0):
            sumZer = sumZer+1
    print(format(sumPos/len(arr),'.6f'))
    print(format(sumNeg/len(arr),'.6f'))
    print(format(sumZer/len(arr),'.6f'))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)