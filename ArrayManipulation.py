#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    index_a = 0
    index_b = 0
    val = 0
    array = [0 for i in range(n)]
    for i in queries:
        index_a = i[0]
        index_b = i[1]
        val = i[2]
        
        array[index_a-1] = array[index_a-1] + val
        if index_b < n:
            array[index_b] = array[index_b] - val
    sum1 = 0
    maximum = 0
    for i in array:
        sum1 = sum1 + i
        maximum = max(sum1, maximum)
            
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
