#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    # Write your code here
    array = []
    Collections = collections.Counter(stringList)
    uniqueElements = list(Collections.keys())
    occurances = list(Collections.values())
    print(uniqueElements)
    print(occurances)
    for i in queries:
        if i in uniqueElements:
            print(i)
            array.append(occurances[uniqueElements.index(i)])
        else:
            array.append(0)
            
    return array
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
