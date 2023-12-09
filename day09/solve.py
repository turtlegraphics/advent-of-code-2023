#
# Advent of Code 2023
# Bryan Clair
#
# Day 09
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

# import re
# parser = re.compile(r"name:\s*(\w+)\s*val:\s*(\d+)") # or whatever
# name, val = parser.match(line).groups()
# val = int(val)

part1, part2 = 0,0

import numpy as np

def binom(n,k):
    val = 1
    while k > 0:
        val *= n/k
        n -= 1
        k -= 1
    return val

def seq(coeffs,t):
    """Evaluate the polynomial with coeffs at t"""
    val = 0
    for i in range(len(coeffs)):
        val += coeffs[i]*binom(t,i)
    return(val)

for line in inputlines:
    x =  [int(x) for x in line.split()]
    coeffs = []
    while (np.any(x)):
        coeffs.append(x[0])
        x = np.diff(x)
    part1 += seq(coeffs,len(line.split()))
    part2 += seq(coeffs,-1)

print('part1:',part1)
print('part2:',part2)
