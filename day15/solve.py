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
    for i in range(len(boxes)):
        if boxes[i]:
            print('Box',i,':',boxes[i])

boxes = []
for i in range(256):
    boxes.append([])

import re
    
for step in prog:
    label, op, val = re.match(r'([a-z]+)([=-])(.*)',step).groups()
    h = hash(label)
    if op == '-':
        for i in range(len(boxes[h])):
            (l,v) = boxes[h][i]
            if label == l:
                boxes[h].pop(i)
                break
    else:
        found = False
        for i in range(len(boxes[h])):
            (l,v) = boxes[h][i]
            if label == l:
                boxes[h][i] = (l,val)
                found = True
                break
        if not found:
            boxes[h].append((label,val))

for b in range(len(boxes)):
    for slot in range(len(boxes[b])):
        (l,v) = boxes[b][slot]
        part2 += (b+1)*(slot+1)*int(v)
        
print('part2:',part2)
