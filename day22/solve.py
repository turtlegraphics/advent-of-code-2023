#
# Advent of Code 2023
# Bryan Clair
#
# Day 22
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

part1, part2 = 0,0

class Brick:
    def __init__(self,id,e1,e2):
        if id < 26:
            self.id = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[id]
        else:
            self.id = str(id)
            
        self.ends = [e1,e2]
        self.orient = 2  # default to z orientation for single cubes
        for i in range(3):
            if e1[i] != e2[i]:
                self.orient = i
                if e1[i] > e2[i]:
                    self.ends = [e2,e1]
        self.xmin = min(e1[0],e2[0])
        self.xmax = max(e1[0],e2[0])
        self.ymin = min(e1[1],e2[1])
        self.ymax = max(e1[1],e2[1])
        self.zmin = min(e1[2],e2[2])
        self.zmax = max(e1[2],e2[2])
        self.ispole = (self.zmax > self.zmin)
        self.supporting = []
        self.supported_on = []
        self.stable = (self.zmin == 1)
            
    def __str__(self):
        out = "%3s: " % self.id
        out += 'xyz'[self.orient]
        out += str(self.ends)
        if self.stable:
            out += 'stable'
        else:
            out += 'fallin'
        out += '\n   supported by:'
        for b in self.supported_on:
            out += b.id + ' '
        out += '\n   supporting:'
        for b in self.supporting:
            out += b.id + ' '
        return out

    def on(self,b):
        """Check if self if resting on b"""
        if b.zmax + 1 != self.zmin:
            return False
        if self.xmin > b.xmax:
            return False
        if self.xmax < b.xmin:
            return False
        if self.ymin > b.ymax:
            return False
        if self.ymax < b.ymin:
            return False
        return True

    def crucial(self):
        """Decide if disintegrating this block would move something else"""
        for b in self.supporting:
            if len(b.supported_on) == 1:
                return True
        return False
    
    def drop(self):
        """Return if you moved."""
        assert(self in ztable[self.zmin])
        if self.stable:
            return False

        for dz in range(maxpole+1):
            z = self.zmin - 1 - dz
            if z < 1:
                continue
            for b in ztable[z]:
                # print('is',self.id,'on',b.id,':',self.on(b))
                if self.on(b):
                    self.stable = True
                    self.supported_on.append(b)
                    b.supporting.append(self)

        if self.stable:
            return False
        
        ztable[self.zmin].remove(self)
        self.zmin -= 1
        self.zmax -= 1
        ztable[self.zmin].append(self)

        if self.zmin == 1:
            self.stable = True
            self.supported_on = []
            
        return True
    
bricks = []

ceiling = 0
maxpole = 1
id = 0
for line in inputlines:
    e1,e2 = line.split('~')
    
    b = Brick(id, [int(x) for x in e1.split(',')],
              [int(x) for x in e2.split(',')])
    bricks.append(b)
    ceiling = max(ceiling, b.zmax)
    maxpole = max(maxpole, b.zmax - b.zmin)
    id += 1
ceiling += 1

ztable = []
for z in range(ceiling):
    ztable.append([])

for b in bricks:
    ztable[b.zmin].append(b)

moved = True
count = 1
while moved:
    moved = False
    for z in range(2,ceiling):
        layer = ztable[z].copy()
        for b in layer:
            if b.drop():
                moved = True
    count += 1

for b in bricks:
    if not b.crucial():
        part1 += 1

for thebrick in bricks:
    count = 0
    for b in bricks:
        b.moved = False
        
    thebrick.moved = True

    unstable = thebrick.supporting.copy()
    while unstable:
        b = unstable.pop(0)
        if b.moved:
            continue
        bfall = True
        for b_on in b.supported_on:
            if not b_on.moved:
                bfall = False
        if bfall:
            b.moved = True
            count += 1
            for c in b.supporting:
                unstable.append(c)
    part2 += count
    
print('part1:',part1)
print('part2:',part2)
