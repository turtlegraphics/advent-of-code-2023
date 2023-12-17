#
# Advent of Code 2023
# Bryan Clair
#
# Day 17
#
import sys
import aoc17 as aoc

args = aoc.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]

city = aoc.Grid()
city.scan(inputlines)

for p in city:
    city[p] = int(city[p])
    
source = (0,city.height()-1)
dest = (city.width()-1,0)

def heat_loss(u,v):
    return city[v]

(dist,prev,past) = city.dijkstra(source,dest, distance_function = heat_loss)

print('part1:', dist[(dest,past)])

(dist,prev,past) = city.ultradijkstra(source,dest, distance_function = heat_loss)

# print route
if args.debug:
    d = (dest,past)
    while d:
        try:
            city[d[0]]=d[1][-1]
        except IndexError:
            pass
        d = prev[d]
    print(city)

print('part2:', dist[(dest,past)])
