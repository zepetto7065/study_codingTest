from itertools import combinations
import math

def solution(brown, yellow):
    arr = []
    for i in range(1,yellow+1):
        if yellow % i == 0:
            arr.append(i)
    for x in arr[:math.ceil(len(arr)/2)]:
        h = x+2
        w = int(yellow/x)+2
        if w*h == brown+yellow:
            return [w, h]