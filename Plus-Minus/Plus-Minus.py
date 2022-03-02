#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    postive = 0
    negative = 0
    zero = 0
    
    for i in range(len(arr)):
        if arr[i] > 0:
            postive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zero += 1
    
    print(postive / len(arr))
    print(negative / len(arr))
    print(zero / len(arr))
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
