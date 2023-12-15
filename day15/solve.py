#
# Advent of Code 2023
# Bryan Clair
#
# Day 15
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

prog = open(args.file).read().strip().split(',')

def hash(s):
    v = 0
    for c in list(s):
        v += ord(c)
        v *= 17
        v = v % 256
    return v

part1, part2 = 0,0

for step in prog:
    part1 += hash(step)

print('part1:',part1)

def printboxes():
    for i,box in enumerate(boxes):
        if box:
            print('Box',i,':',box)

boxes = []
for i in range(256):
    boxes.append([])

import re
    
for step in prog:
    label, op, val = re.match(r'([a-z]+)([=-])(.*)',step).groups()
    if val:
        val = int(val)
    h = hash(label)

    if op == '-':
        for i,(l,v) in enumerate(boxes[h]):
            if label == l:
                boxes[h].pop(i)
                break
    if op == '=':
        found = False
        for i,(l,v) in enumerate(boxes[h]):
            if label == l:
                boxes[h][i] = (l,val)
                break
        else:
            boxes[h].append((label,val))

    # print(step)
    # printboxes()
    
for b,box in enumerate(boxes):
    for slot,(l,v) in enumerate(box):
        part2 += (b+1)*(slot+1)*v
        
print('part2:',part2)
