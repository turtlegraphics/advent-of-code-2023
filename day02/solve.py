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
for line in inputlines:
    game,colors = line.split(':')
    game_id = int(game.split(' ')[1])
    # print('Game',game_id)
    game_ok = True
    sets = colors.split(';')
    for s in sets:
        # print('set:',s)
        for c in s.split(','):
            num, col = c.strip().split(' ')
            if int(num) > bagmax[col]:
                game_ok = False
    if game_ok:
        part1 += game_id

print('part1:',part1)
            
    
