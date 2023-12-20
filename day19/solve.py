#
# Advent of Code 2023
# Bryan Clair
#
# Day 19
#
import sys
import aocutils
from aocutils import debug

args = aocutils.parse_args()

rawin = open(args.file).read()

rulesstr, partsstr = rawin.split('\n\n')

import re

def apply(part, workflow):
    """Given a workflow name, return a result which is A, R, or a new rule."""
    steps, default = workflows[workflow]
    for reg,op,val,result in steps:
        # print('test',reg+op+val,result)
        partval = part[reg]
        if op == '<' and partval < val:
            return result
        if op == '>' and partval > val:
            return result
    return(default)

workflows = {}
for r in rulesstr.split('\n'):
    name,stepstr = re.match(r"(\w+){(.*)}",r).groups()
    stepstr = stepstr.split(',')
    steps = []
    for s in stepstr[:-1]:
        reg,op,val,result = re.match(r"(.)(.)(\d+):(\w+)",s).groups()
        reg = 'xmas'.find(reg)
        val = int(val)
        steps.append((reg,op,val,result))
    workflows[name] = (steps,stepstr[-1])

total = 0    
for p in partsstr.strip().split('\n'):
    vals = re.match(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}",p).groups()
    x,m,a,s = [int(v) for v in vals]
    rating = x+m+a+s
    part = (x,m,a,s)
    current = "in"
    while current not in ['A','R']:
        current = apply(part,current)
    if current == 'A':
        total += rating
    
print('part1:',total)

def size(zone):
    s = 1
    for z in zone:
        s *= (z[1]-z[0])
    return s

total = 0
count = 0
zonelist = [(((1,4001),(1,4001),(1,4001),(1,4001)),"in")]
while zonelist:
    count += 1
    if count % 10000 == 0:
        print(count)
    zone,workflow = zonelist.pop(0)
    if workflow == 'A':
        total += size(zone)
        continue
    if workflow == 'R':
        continue
    
    debug('working', zone, size(zone))
    steps, default = workflows[workflow]
    for reg,op,val,result in steps:
        debug('xmas'[reg],op,val,':',result)
        low,high = zone[reg]
        if op == '<':
            accept = None
            reject = None
            if high <= val:
                accept = (low,high)
            elif low < val:
                accept = (low,val)
                reject = (val,high)
            else:
                reject = (low,high)
        if op == '>':
            accept = None
            reject = None
            if low > val :
                accept = (low,high)
            elif high-1 > val:
                accept = (val+1,high)
                reject = (low,val+1)
            else:
                reject = (low,high)

        if accept:
            Azone = [z for z in zone]
            Azone[reg] = accept
            zonelist.append((tuple(Azone),result))
            debug('accept',tuple(Azone))
            
        if reject:
            Rzone = [z for z in zone]
            Rzone[reg] = reject
            zone = tuple(Rzone)
        else:
            break # nothing left
    else:  # if we made it through the for loop
        assert(reject)
        zonelist.append((zone,default))

print('part2:',total)
