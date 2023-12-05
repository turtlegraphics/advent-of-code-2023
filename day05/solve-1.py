#
# Advent of Code 2023
# Bryan Clair
#
# Day 05
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

class range:
    def __init__(self,rstr):
        self.dest, self.source, self.length = [int(x) for x in rstr.strip().split()]

    def convert(self, v):
        if v >= self.source and v < self.source + self.length:
            return v - self.source + self.dest
        else:
            return -1

    def __str__(self):
        out = str(self.source) + ':' + str(self.source + self.length-1)
        out += ' --> ' + str(self.dest) + ':' + str(self.dest + self.length -1)
        return out
    
class map:
    def __init__(self,mapstr):
        self.ranges = [range(s) for s in mapstr[1:]]
        self.source, dash, self.dest = mapstr[0].split()[0].split('-')

    def convert(self, v):
        for r in self.ranges:
            w = r.convert(v)
            if w != -1:
                return w
        return v
    
    def __str__(self):
        out = self.source + ' to ' + self.dest + ' map:\n'
        for r in self.ranges:
            out += str(r) + '\n'
        return out
    
part1, part2 = 0,0

intxt = open(args.file).read()
blocks = intxt.split('\n\n')

maps = {}

seeds = [int(x) for x in blocks[0].split()[1:]]

for b in blocks[1:]:
    lines = b.strip().split('\n')
    m = map(lines)
    maps[m.source] = m

part1 = 10000000000000000000000000

for s in seeds:
    kind = 'seed'
    x = s

    while kind != 'location':
        m = maps[kind]
        x = m.convert(x)
        kind = m.dest

    if x < part1:
        part1 = x
        
print('part1:',part1)
print('part2:',part2)
