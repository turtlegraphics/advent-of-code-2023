#
# Advent of Code 2023
# Bryan Clair
#
# Day 14
#
import sys
sys.path.append("..")
import aocutils

class Platform(aocutils.Grid):
    def roll_n(self):
        moved = False
        y = self.ymax - 1
        while y >= self.ymin:
            for x in range(self.xmin,self.xmax+1):
                if self[x,y] == 'O' and self[x,y+1] == '.':
                    moved = True
                    self[x,y] = '.'
                    self[x,y+1] = 'O'
            y -= 1
        return moved

    def roll_s(self):
        moved = False
        y = self.ymin + 1
        while y <= self.ymax:
            for x in range(self.xmin,self.xmax+1):
                if self[x,y] == 'O' and self[x,y-1] == '.':
                    moved = True
                    self[x,y] = '.'
                    self[x,y-1] = 'O'
            y += 1
        return moved
    
    def roll_e(self):
        moved = False
        x = self.xmax - 1
        while x >= self.xmin:
            for y in range(self.ymin,self.ymax+1):
                if self[x,y] == 'O' and self[x+1,y] == '.':
                    moved = True
                    self[x,y] = '.'
                    self[x+1,y] = 'O'
            x -= 1
        return moved

    def roll_w(self):
        moved = False
        x = self.xmin + 1
        while x <= self.xmax:
            for y in range(self.ymin,self.ymax+1):
                if self[x,y] == 'O' and self[x-1,y] == '.':
                    moved = True
                    self[x,y] = '.'
                    self[x-1,y] = 'O'
            x += 1
        return moved
    
    def load(self):
        l = 0
        for y in range(self.ymin,self.ymax+1):
            for x in range(self.xmin,self.xmax+1):
                if self[x,y] == 'O':
                    l += y+1
        return l

    def cycle(self):
        while (platform.roll_n()):
            pass
        while (platform.roll_w()):
            pass
        while (platform.roll_s()):
            pass
        while (platform.roll_e()):
            pass
    
args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

platform = Platform()
platform.scan(inputlines)

while (platform.roll_n()):
    pass
print('part1:',platform.load())

platform = Platform()
platform.scan(inputlines)

seen = {}

i = 0
done = False
while not done:
    platform.cycle()
    i += 1
    if (i % 10 == 0):
        print('...',i)
    if str(platform) in seen:
        print('found it at', i)
        print('seen before at',seen[str(platform)])
        cycle_start = seen[str(platform)]
        cycle_length = i - cycle_start
        done = True
    else:
        seen[str(platform)] = i

goal = 1000000000
skips = (goal - cycle_start) // cycle_length
i = cycle_start + skips * cycle_length
print(i)

assert(i <= goal)

while i < goal:
    platform.cycle()
    i += 1
    if (i % 10 == 0):
        print('...',i)
    
print('part2:',platform.load())

    
