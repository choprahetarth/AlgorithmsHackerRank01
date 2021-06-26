#!/bin/python3
# https://www.hackerrank.com/challenges/the-power-sum/problem

import math
import os
import random
import re
import sys

def recursive(X,N,i):
    sumToBeDeleted = i**N
    if (sumToBeDeleted>X):
        return 0
    elif (sumToBeDeleted == X):
        return 1
    else:
        return recursive(X,N,i+1)+recursive(X-sumToBeDeleted,N,i+1)
 # Complete the powerSum function below.
def powerSum(X, N):
    a = recursive(X,N,1)
    return a


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
