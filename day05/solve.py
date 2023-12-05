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

class MapRange:
    def __init__(self,rstr):
        self.dest, self.source, self.length = [int(x) for x in rstr.strip().split()]

    def convert(self, v):
        if self.source <= v < self.source + self.length:
            return v - self.source + self.dest
        else:
            return -1

    def convertlist(self, vals):
        """vals is a list of (start, length) pairs.
        Returns two lists, the converted and the unconverted values."""
        converted = []
        unconverted = []
        totlen = 0
        # print('converting',self.source,self.length)
        for (start,length) in vals:
            totlen += length  # for error checking
            if start < self.source:
                #print('unc1',start,length,self.source,self.length)
                # unconverted piece at beginning
                cliplen = min(length, self.source - start)
                unconverted.append((start,cliplen))
                start += cliplen
                length -= cliplen
                if length == 0:
                    continue
            if start < self.source + self.length:
                #print('conv',start,length,self.source,self.length)
                # convert piece in the middle
                cliplen = min(length, self.source + self.length - start)
                converted.append((start - self.source + self.dest,cliplen))
                start += cliplen
                length -= cliplen
                if length == 0:
                    continue
            assert(start >= self.source + self.length)
            #print('unc2',start,length,self.source,self.length)
            unconverted.append((start,length))

        clen = 0
        ulen = 0
        for (start,length) in converted:
            clen += length
        for (start,length) in unconverted:
            ulen += length
        #print(totlen,'-->',clen,'(c) ', ulen,'(u)')

        return converted, unconverted
    
    def __str__(self):
        out = str(self.source) + ':' + str(self.source + self.length-1)
        out += ' --> ' + str(self.dest) + ':' + str(self.dest + self.length -1)
        return out
    
class Map:
    def __init__(self,mapstr):
        self.ranges = [MapRange(s) for s in mapstr[1:]]
        self.source, _, self.dest = mapstr[0].split()[0].split('-')

    def convert(self, v):
        for r in self.ranges:
            w = r.convert(v)
            if w != -1:
                return w
        return v

    def convertlist(self, vals):
        converted = []
        unconverted = vals
        for r in self.ranges:
            c, unconverted = r.convertlist(unconverted)
            converted.extend(c)
            
        converted.extend(unconverted)
        return converted
    
    def __str__(self):
        out = self.source + ' to ' + self.dest + ' map:\n'
        for r in self.ranges:
            out += str(r) + '\n'
        return out
    
seeds, *blocks = open(args.file).read().split('\n\n')
seeds = [int(x) for x in seeds.split()[1:]]

maps = {}

for b in blocks:
    lines = b.strip().split('\n')
    m = Map(lines)
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

seedranges = []
for i in range(0,len(seeds),2):
    seedranges.append((seeds[i],seeds[i+1]))

part2 = 10000000000000000000000000
kind = 'seed'
x = seedranges
while kind != 'location':
    m = maps[kind]
    x = m.convertlist(x)
    kind = m.dest

for (s,l) in x:
    if s < part2:
        part2 = s
        

print('part2:',part2)
