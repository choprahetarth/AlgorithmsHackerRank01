#!/bin/python3

import math
import os
import random
import re
import sys
import operator


cost = []
costMatrix= [] 
sumMatrixBefore = []
# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    magicReference()
    finalCost = compareFunction(s)
    return finalCost

def compareFunction(givenList):
    global cost
    givenList = givenList+givenList+givenList+givenList+givenList+givenList
    for i in range(18):
        for c in range(3):
            tempCost = givenList[i][c] - referenceSquare[i][c]
            cost.append(abs(tempCost))
    chunks = [cost[x:x+3] for x in range(0, len(cost), 3)] # used to club all the data into multiples of three
    for i in range(18):
        tempSumVariable = sum(chunks[i])
        sumMatrixBefore.append(tempSumVariable)
    smallerChunks = [sumMatrixBefore[x:x+3] for x in range(0, len(sumMatrixBefore), 3)] # used to club all the data into multiples of three
    for i in range(6):
        tempSumVariable = sum(smallerChunks[i])
        costMatrix.append(tempSumVariable)
    print(costMatrix)
    return min(costMatrix)


def magicReference():
    global referenceSquare
    originalSquare = [[8,3,4], [1,5,9], [6,7,2]] 
    newSquare1 = rotate(originalSquare)
    newSquare2 = rotate(newSquare1)
    newSquare3 = rotate(newSquare2)
    newSquare4 = reflect(originalSquare, "row")
    newSquare5 = reflect(originalSquare, "column")
    newSquare6 = transpose(originalSquare)
    referenceSquare = newSquare1+newSquare2+newSquare3+newSquare4+newSquare5+newSquare6
    
def transpose(square):
    newSquare = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for c in range(3):
           newSquare[i][c] = square[c][i] 
    return newSquare 


def rotate(square):
    newSquare = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for c in range(3):
           newSquare[i][c] = square[c][2-i] 
    return newSquare

def reflect(square2, parameter):
    newSquare = [[0,0,0],[0,0,0],[0,0,0]]
    if (parameter == "row"):
        for i in range(3):
            for c in range(3):
                newSquare[i][c] = square2[i][2-c]  
    elif (parameter == "column"):
        for i in range(3):
            for c in range(3):
                newSquare[c][i] = square2[2-c][i]  
    return newSquare


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
