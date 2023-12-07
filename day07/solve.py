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

ranks = list('J23456789TQKA')

values = {}
val=1
for r in ranks:
    values[r] = val
    val += 1
    
def val(line):
    hand,bid = line.split()
    counts = [0]*len(ranks)
    pairs = 0
    for i in range(len(ranks)):
        counts[i] = hand.count(ranks[i])
        if counts[i] == 2 and i > 0:
            pairs += 1
            
    jokers = counts[0]
    counts[0] = 0
    val = max(counts) + jokers
    
    if val == 2 and pairs == 2:
        val = 2.5
    if val == 3 and (pairs == 2 or (pairs == 1 and jokers==0)):
        val = 3.5

    quality = [val]
    for h in list(hand):
        quality.append(values[h])

#    print(hand,val,jokers,counts, quality)
    return tuple(quality)

winnings = 0
rank = 1
for line in sorted(inputlines, key=val):
#    print(rank,line,val(line))
    hand,bid = line.split()
    winnings += rank*int(bid)
    rank += 1

print('winnings (part2):', winnings)
