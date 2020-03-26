#!/bin/python3
# https://www.hackerrank.com/challenges/the-power-sum/problem?isFullScreen=true
# THIS IS NOT AN OPTIMAL SOLUTION, I STILL HAVE TO LEARN DP AND RECURSION

import math
import os
import random
import re
import sys

def recursive(var,N):
    temp = var - ((math.floor(var**(1/N)))**N)
    print(temp)
    return temp

def canComplete(summer):
    global stopLoopFlag
    stopLoopFlag = 0
    while(stopLoopFlag!=1):
        summer = recursive(summer,N)
        if (summer==0):
            canComplete = 1
            stopLoopFlag = 1
        elif(summer<0):
            canComplete = 0
            stopLoopFlag = 1
        elif(summer>0):
            stopLoopFlag = 0
    return canComplete


 # Complete the powerSum function below.
def powerSum(X, N):
    resultMatrix = []
    a = canComplete(X)
    resultMatrix.append(a)
    bareboneRank = math.floor(X**(1/N))
    newSum = math.floor(X**(1/N))**N
    #if (a ==1):
        #check for other solutions
        #for c in range(bareboneRank):
        #    a = canComplete(newSum-c)
        #    resultMatrix.append(a)
    #print(resultMatrix)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    #fptr.write(str(result) + '\n')

    #fptr.close()