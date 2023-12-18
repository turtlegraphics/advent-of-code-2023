#
# Advent of Code 2023
# Bryan Clair
#
# Day 18
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

part1, part2 = 0,0

pos = aocutils.Point(0,0)

dirs = {
    '0': aocutils.Point(1,0),
    '2': aocutils.Point(-1,0),
    '3': aocutils.Point(0,1),
    '1': aocutils.Point(0,-1)
    }

# compute the curve integral y dx - x dy
integral = 0
length = 0
for line in inputlines:
    _, _, color = line.split()
    
    distance = int(color[2:7],16)
    heading = dirs[color[7]]*distance
    
    length += distance
    
    integral += -pos.x*heading.y + pos.y*heading.x
    pos += heading

print('part2:', integral/2 + length/2 + 1)
