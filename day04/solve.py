#
# Advent of Code 2023
# Bryan Clair
#
# Day 04
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
copies = [1]*len(inputlines)

id = 0
for line in inputlines:
    card, nums = line.split(':')
    assert(id == int(card.split()[1])-1)
    
    winners, have = nums.split('|')
    winners = [int(x) for x in winners.strip().split()]
    have = [int(x) for x in have.strip().split()]
    val = 1
    matches = 0
    for x in have:
        if x in winners:
            val *= 2
            matches += 1
    val = val//2
    part1 += val
    for k in range(matches):
        try:
            copies[id + k + 1] += copies[id]
        except IndexError:
            pass
    id += 1

for k in copies:
    part2 += k
    
print('part1:',part1)
print('part2:',part2)
