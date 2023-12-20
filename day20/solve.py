#
# Advent of Code 2023
# Bryan Clair
#
# Day 20
#
import sys
import aocutils

args = aocutils.parse_args()
inputlines = [x.strip() for x in open(args.file).readlines()]

class Module:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections
        self.typestr = ''
        
    def __str__(self):
        return self.typestr + self.name + str(self.connections)

    def connect(self,name):
        """Not used generically."""
        pass

    def send(self, mfrom, pulse):
        # print(mfrom,pulse,'->',self.name)
        events.append((mfrom, self.name, pulse))

    def receive(self, mfrom, pulse):
        # print(self, 'received', pulse)
        val = self.process(mfrom, pulse)
        if val is not None:
            for m in self.connections:
                # print(self,val,'->',m)
                modules[m].send(self.name, val)

class FlipFlop(Module):
    def __init__(self, name, connections):
        Module.__init__(self,name,connections)
        self.typestr = '%'
        self.state = False
        
    def process(self, who, pulse):
        if pulse:
            # ignore
            return None
        
        self.state = not self.state
        return self.state

class Conjunction(Module):
    def __init__(self, name, connections):
        Module.__init__(self,name,connections)
        self.typestr = '&'
        self.states = {}  # track state of inputs
        self.watching = False
        
    def connect(self,name):
        """This is how we tell a conjunction about an input and initialize it."""
        self.states[name] = False
        
    def process(self, who, pulse):
        self.states[who] = pulse
        out = True
        for i in self.states:
            out = out and self.states[i]
        out = not out
        if out and self.watching:
            # print(self.name, button_count)
            periods.append(button_count)
            self.watching = False
        return out

    def states_on(self):
        onstates = 0
        for i in self.states:
            if self.states[i]:
                onstates += 1
        return onstates
    
    def __str__(self):
        out = Module.__str__(self)
        out += str(self.states)
        return out
            
class Broadcaster(Module):
    def process(self, who, pulse):
        return pulse

class Output(Module):
    def process(self, who, pulse):
        if pulse == False:
            # sometime after the universe dies:
            print('solved after',button_press,'steps')

    def connect(self, who):
        self.trigger = who
        
def button():
    global events
    events = []
    low = 0
    high = 0
    events.append(('button','broadcaster',False))

    while events:
        mfrom, mto, pulse  = events.pop(0)
        if pulse:
            high += 1
        else:
            low += 1
        modules[mto].receive(mfrom,pulse)

    return (low,high)

modules = {}
for line in inputlines:
    mname, connections = line.split(' -> ')
    connections = [x.strip() for x in connections.split(',')]
    if mname[0] == '%':
        m = FlipFlop(mname[1:], connections)
    elif mname[0] == '&':
        m = Conjunction(mname[1:], connections)
    else:
        assert(mname == 'broadcaster')
        m = Broadcaster(mname, connections)
      
    modules[m.name] = m

# run through and tell each module who its inputs are
# also locates the "output" module, if there is one
outmod = None
for m in modules:
    for c in modules[m].connections:
        try:
            modules[c].connect(m)
        except KeyError:
            outmod = Output(c, [])
            outmod.connect(m)

if outmod:
    modules[outmod.name] = outmod
    trigger = outmod.trigger
    for c in modules[trigger].states.keys():
        modules[c].watching = True
    
events = []

part1_low = 0
part1_high = 0

button_count = 0
periods = []


while button_count < 8000:
    button_count += 1
    low,high =  button()
    for m in modules:
        try:
            modules[m].button_done(button_count)
        except AttributeError:
            pass
        
    part1_low += low
    part1_high += high
    if button_count == 1000:
        print('part1:',part1_low * part1_high)

# print('periods:',periods)

from math import gcd
lcm = 1
prod = 1
for p in periods:
    prod *= p
    lcm = lcm*p//gcd(lcm, p)

assert(prod == lcm)

print('part2:', prod)
