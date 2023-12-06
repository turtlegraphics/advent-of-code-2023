#
# Advent of Code 2023
# Bryan Clair
#
# Day 06
#
import sys
sys.path.append("..")
import aocutils
import math

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

time = [int(x) for x in inputlines[0].split()[1:]]
distance = [int(x) for x in inputlines[1].split()[1:]]


# import re
# parser = re.compile(r"name:\s*(\w+)\s*val:\s*(\d+)") # or whatever
# name, val = parser.match(line).groups()
# val = int(val)

part1, part2 = 0,0

def wins(t,d):
    count = 0
    for b in range(t+1):
        if b*(t-b) > d:
            count += 1
    return count

def xwins(t,d):
    disc = math.sqrt(t*t - 4*d)
    return math.floor((t+disc)/2) - math.ceil((t-disc)/2) + 1

part1 = 1
for i in range(len(time)):
    part1 *= wins(time[i],distance[i])

fulltime = int(''.join(inputlines[0].split(':')[1].split()))
fulldist = int(''.join(inputlines[1].split(':')[1].split()))

part2 = xwins(fulltime, fulldist)
# part2 = wins(fulltime, fulldist) # this only took like 5 seconds

print('part1:',part1)
print('part2:',part2)
