#
# Advent of Code 2023
# Bryan Clair
#
# Day 08
#
import sys
sys.path.append("..")
import aocutils
from math import lcm

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

import re
parser = re.compile(r"(\w+) = \((\w+), (\w+)\)") # or whatever
# val = int(val)

part1, part2 = 0,0

map = {}
map['L'] = {}
map['R'] = {}

instructions = list(inputlines[0])
startnodes = []
for line in inputlines[2:]:
    a, l, r = parser.match(line).groups()
    map['L'][a] = l
    map['R'][a] = r
    if a[2] == 'A':
        startnodes.append(a)

current = 'AAA'
spot = 0
while current != 'ZZZ':
    turn = instructions[spot]
    current = map[turn][current]
    spot = (spot+1) % len(instructions)
    part1 += 1

print('part1:',part1)

lengths = []
for start in startnodes:
    current = start
    spot = 0
    length = 0
    while current[2] != 'Z':
        turn = instructions[spot]
        current = map[turn][current]
        spot = (spot+1) % len(instructions)
        length += 1
    lengths.append(length)

print('part2:',lcm(*lengths))
