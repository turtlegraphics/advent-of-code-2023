#
# Advent of Code 2023
# Bryan Clair
#
# Day 07
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

ranks = list('23456789TJQKA')

values = {}
val=2
for r in ranks:
    values[r] = val
    val += 1
    
def val(line):
    hand,bid = line.split()
    counts = [0]*len(ranks)
    pairs = 0
    for i in range(len(ranks)):
        counts[i] = hand.count(ranks[i])
        if counts[i] == 2:
            pairs += 1
    val = max(counts)
    if val == 2 and pairs == 2:
        val = 2.5
    if val == 3 and pairs == 1:
        val = 3.5

    quality = [val]
    for h in list(hand):
        quality.append(values[h])

    return tuple(quality)

part1, part2 = 0,0

rank = 1
for line in sorted(inputlines, key=val):
    #print(rank,line,val(line))
    hand,bid = line.split()
    part1 += rank*int(bid)
    rank += 1

print('part1:',part1)
print('part2:',part2)
