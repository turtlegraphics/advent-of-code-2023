#
# Advent of Code 2023
# Bryan Clair
#
# Day 02
#
import sys
sys.path.append("..")
import aocutils

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

bagmax = {
    'red':12,
    'green':13,
    'blue':14
    }

part1 = 0
part2 = 0
for line in inputlines:
    game,colors = line.split(':')
    game_id = int(game.split(' ')[1])
    # print('Game',game_id)
    game_ok = True
    minset = {
        'red':0,
        'green':0,
        'blue':0
    }
    sets = colors.split(';')
    for s in sets:
        # print('set:',s)
        for c in s.split(','):
            num, col = c.strip().split(' ')
            num = int(num)
            if num > bagmax[col]:
                game_ok = False
            minset[col] = max(minset[col],num)
            
    if game_ok:
        part1 += game_id
    part2 += minset['red']*minset['green']*minset['blue']

print('part1:',part1)
print('part2:',part2)
            
    
