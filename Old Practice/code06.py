#!/bin/python3

import math
import os
import random
import re
import sys




# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    print(scores)
    for i in range(len(alice)):
        tempArray = []
        tempArray.clear()
        tempArray = scores
        tempArray.append(alice[i])
        newRanks = denseRanking(tempArray)
        print(newRanks.pop())

def denseRanking(scores):
    finalScoreVector = []
    scoreDictionary = {}
    sortedScores = list(set(scores))
    sortedScores.sort(reverse=True)
    rankCountList = list(range(1,len(set(sortedScores))+1))# set only takes in the unique values
    for i in range(len(sortedScores)):
        scoreDictionary[sortedScores[i]] = rankCountList[i]
    for i in range(len(scores)):
        tempScore = scores[i]
        finalScoreVector.append(scoreDictionary[tempScore])
    return(finalScoreVector)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())``

    alice = list(map(int, input().rstrip().split()))


    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
