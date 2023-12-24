#
# Advent of Code 2023
# Bryan Clair
#
# Day 24
#
import sys
sys.path.append("..")
import aocutils
from aocutils import debug
import math

args = aocutils.parse_args()

inputlines = [x.strip() for x in open(args.file).readlines()]
part1, part2 = 0,0

hail = []
for line in inputlines:
    sp,sv = line.split(' @ ')
    p = aocutils.Point3d([int(v) for v in sp.split(',')])
    v = aocutils.Point3d([int(v) for v in sv.split(',')])
    hail.append((p,v))

def intersect(h1,h2):
    testmin = 200000000000000
    testmax = 400000000000000
    
    p1,v1 = h1
    p2,v2 = h2
    p0 = p1 - p2
    a = v2.x
    b = -v1.x
    c = v2.y
    d = -v1.y
    det = a*d-b*c
    if (det == 0):
        # paths are parallel
        if v1.y*p0.x == v1.x*p0.y:
            # same path
            debug("whoa!")
            return 1
        else:
            debug("whiff")
            return 0
    
    sdet = p0.x*d - p0.y*b
    tdet = -p0.x*c + p0.y*a
    assert(det*p1.x + tdet*v1.x == det*p2.x + sdet*v2.x)
    assert(det*p1.y + tdet*v1.y == det*p2.y + sdet*v2.y)
    s = sdet/det
    t = tdet/det
    if s >= 0 and t >= 0:
        cross = p1 + v1*t
        if testmin <= cross.x <= testmax and testmin <= cross.y <= testmax:
            debug('bang')
            return 1
        else:
            debug('outside')
            return 0
    debug('nope')
    return 0

for i in range(len(hail)):
    for j in range(i):
        h1 = hail[i]
        h2 = hail[j]
        part1 += intersect(h1,h2)

print('part1:',part1)


def location(h,t):
    p,v = h
    return (p + v*t)

def goal(h1,h2,h3,t):
    """Want this to be zero.  turned out to be not helpful."""
    t1,t2,t3 = t
    vec = location(h1,t1)*(t2-t3) + location(h2,t2)*(t3-t1) + location(h3,t3)*(t1-t2)
    return vec.x**2 + vec.y**2 + vec.z**2

dirs = [
    aocutils.Point3d(1,0,0),
    aocutils.Point3d(-1,0,0),
    aocutils.Point3d(0,1,0),
    aocutils.Point3d(0,-1,0),
    aocutils.Point3d(0,0,1),
    aocutils.Point3d(0,0,-1)
    ]
    
def seek(h1,h2,h3):
    """
    Just garbage, nothing to see here. Trying to solve a system of
    equations that were simple to solve with Sage
    """
    t = aocutils.Point3d(1,2,3)
    g = goal(h1,h2,h3,t)
    print('initial',g)
    best = g
    while g > 0:
        print('g',g,'t',t)
        bestdir = None
        for delt in dirs:
            newt = t + delt*0.1
            if newt.x < 0 or newt.y < 0 or newt.z < 0:
                continue
            gtry = goal(h1,h2,h3,newt)
            if gtry < best:
                best = gtry
                bestdir = delt
        g = best
        t = t + bestdir*0.1

def linedist(h1,h2):
    """Return distance between two lines.  Unused."""
    p1,v1 = h1
    p2,v2 = h2
    c = v1.cross(v2)
    return (p1-p2).dot(c)/c.length()

def alldists(h0):
    """Could try to optimize this, but that was worthless."""
    dtot = 0
    for h in hail:
        dtot += linedist(h0,h)**2
    return dtot

def quality(s,t):
    """Try to find s,t that make this zero.  No help."""
    p1,v1 = hail[0]
    p2,v2 = hail[1]
    p = p1 + v1*s
    v = p2 + v2*t - p
    return alldists((p,v))

#
# Begin actual solution to part 2
#

print('\n-- PART 2 --')
ps = []
vs = []
for i in range(4):
    p,v = hail[i]
    ps.append(tuple(p))
    vs.append(tuple(v))


# with some time and paper, you can derive:
print("   the intersection times t1,t2,t3 with stones 1,2,3 must satisfy this system of equations")
equation = '%d*t1 + %d*t2 + %d*t3 + %d*t1*t2 + %d*t2*t3 + %d*t3*t1 == 0'
for c in range(3):
    print('     ',
        equation % (ps[3][c] - ps[2][c],
                    ps[1][c] - ps[3][c],
                    ps[2][c] - ps[1][c],
                    vs[1][c] - vs[2][c],
                    vs[2][c] - vs[3][c],
                    vs[3][c] - vs[1][c])
        )

# now plug this into Sage:
"""
var('t1 t2 t3')
eq1 = 119430253791072*t1 + -30085342142751*t2 + -89344911648321*t3 + -144*t1*t2 + 81*t2*t3 + 63*t3*t1 == 0
eq2 = 173903800293361*t1 + 41276723568456*t2 + -215180523861817*t3 + -333*t1*t2 + 115*t2*t3 + 218*t3*t1 == 0
eq3 = -51579005107740*t1 + 243580154810417*t2 + -192001149702677*t3 + -268*t1*t2 + 245*t2*t3 + 23*t3*t1 == 0
solve([eq1,eq2,eq3],t1,t2,t3)
"""
# which results in this:
"""
[[t1 == r1, t2 == r1, t3 == r1], [t1 == 1/377*sqrt(499704955193435390038880650419) - 459684368383334/377, t2 == 1/377*sqrt(499704955193435390038880650419) - 459684368383334/377, t3 == 1/377*sqrt(499704955193435390038880650419) - 459684368383334/377], [t1 == -1/377*sqrt(499704955193435390038880650419) - 459684368383334/377, t2 == -1/377*sqrt(499704955193435390038880650419) - 459684368383334/377, t3 == -1/377*sqrt(499704955193435390038880650419) - 459684368383334/377], [t1 == 690178246339, t2 == 641672179554, t3 == 106316566481], [t1 == (13270028199008/9), t2 == (13270028199008/9), t3 == (13270028199008/9)]]
"""

t1 = 690178246339
t2 = 641672179554
t3 = 106316566481

print('   that system has one integer solution (thanks to Sage):')
print('     t1=%d, t2=%d, t3=%d' % (t1,t2,t3))

# these are the same, they are the initial velocity of the stone
# print((location(hail[1],t1) - location(hail[2],t2))/(t1-t2))
# print((location(hail[2],t2) - location(hail[3],t3))/(t2-t3))
#print((location(hail[3],t3) - location(hail[1],t1))/(t3-t1))

print("   now solve for the stone's initial velocity")
stone_v = (location(hail[1],t1) - location(hail[2],t2))/(t1-t2)
print('     ',stone_v)


print("   now solve for the stone's initial position")
stone_p = location(hail[1],t1) - stone_v*t1
print('     ',stone_p)

print('\npart2:',round(stone_p.x+stone_p.y+stone_p.z))
