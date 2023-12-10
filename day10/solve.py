#
# Advent of Code 2023
# Bryan Clair
#
# Day 10
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

field = aocutils.Grid()
field.scan(inputlines)

nest = aocutils.Grid()
# find start S
for p in field:
    if field[p] == 'S':
        start = p
    nest[p] = '.'


def step(p,d):
    what = field[p]
    if what == '.':
        raise KeyError('.')
    
    if what == 'L':
        if d.x:
            d = aocutils.Point((0,1))
        else:
            d = aocutils.Point((1,0))
            
    if what == '7':
        if d.x:
            d = aocutils.Point((0,-1))
        else:
            d = aocutils.Point((-1,0))

    if what == 'F':
        if d.x:
            d = aocutils.Point((0,-1))
        else:
            d = aocutils.Point((1,0))

    if what == 'J':
        if d.x:
            d = aocutils.Point((0,1))
        else:
            d = aocutils.Point((-1,0))

    # for - and |, d is unchanged

    p += d
    what = field[p] # throw error if off grid
    
    return (p,d)

# for start_d in field._dirs[:4]:
start_d = (0,-1)
if True:
    p = aocutils.Point(start)
    print('--')
    d = aocutils.Point(start_d)
    print ('heading',d)
    steps = 0
    done = False
    while not done:
        nest[p] = field[p]
        try:
            # print('  ',p)
            (p,d) = step(p,d)
            steps += 1
        except KeyError:
            print('direction',d,'failed')
            done = True
            break
        
        if field[p] == 'S':
            print('at',p,'facing',d,'seeing',field[p])
            print('after',steps,'steps.')
            done = True

        if steps == 100000:
            print('giving up after 100 steps')
            done = True
            
part1 = steps / 2
print('part1:',part1)

part2 = 0

nest[start] = '|'

for p in nest:
    if nest[p] != '.':
        continue
    q = aocutils.Point(p)
    hits = 0
    goal = '|'
    while q.x >= 0:
        # print(nest[q],goal)
        if nest[q] == goal:
            hits += 1
        if nest[q] == '7':
            goal = 'L'
        if nest[q] == 'J':
            goal = 'F'
        if nest[q] == 'F' or nest[q] == 'L':
            goal = '|'
            
        q.x -= 1
    if hits % 2 == 0:
        nest[p] = ','
    else:
        nest[p] = 'I'
        # print('hit',p)
        part2 += 1

print('part2:',part2)
