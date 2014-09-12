import sys

class Node:

    def __init__(self):
        self.kind = -1 #Can either be 0, 1, or 2 meaning empty, wall, or ramen
        self.has_person = 0 #for knowing the current location
        self.g = 0 #g value for a*
        self.h = 0 #h value for a*
        self.f = 0 #f value for a*
        self.parent = [0, 0] #for determining path; may not need since every step is required to be drawn

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        self.kind = kind

    def get_g(self):
        return self.g

    def set_g(self, g):
        self.g = g

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f

    def get_parent(self):
        return self.parent

    def set_paret(self, parent):
        self.parent = parent

    def set_occupied(self, x):
        self.has_person = x

    def get_occupied(self):
        return self.has_person

#takes grid as input, and prints to screen what original input file looks like but with updated locations for the '@' symbol
def display_grid():
    for n in range(0, len(grid)):
        line_str = ''
        for x in range(0, len(grid[n])):
            if grid[n][x].get_occupied == 1:
                line_str += '@'
            elif  grid[n][x].get_kind == 0:
                line_str = line_str + '.'
                print 'omg'
            elif  grid[n][x].get_kind == 1:
                line_str = line_str + '#'
            elif  grid[n][x].get_kind == 2:
                line_str = line_str + '%'
        print line_str
        print 'doing something'


#file IO. Taken from lecture slides
if(len(sys.argv)) != 2: 
    #notice sys.argv is a list of command-line args and we found its length
    print "Please supply a filename"
    raise SystemExit(1) # throw an error and exit
f = open(sys.argv[1]) #program name is argv[0]
lines = f.readlines() # reads all lines into list one go
f.close()

#this cleans up the lines and makes each line into a list itself. This will be used to cunstruct the list of nodes
for n in range(0, len(lines)):
    lines[n] = list(lines[n].strip()) 


print lines #for debug purposes currently 


grid = []

for n in range(0, len(lines)):
    li = []
    for x in range(0, len(lines[n])):
        node = Node()
        if lines[n][x] == '.' or lines[n][x] == '@':
            node.set_kind(0)
        if lines[n][x] == '#':
            node.set_kind(1)
        if lines[n][x] == '%':
            node.set_kind(2)
        #TODO: set other node properties
        li.append(node)
    grid.append(li)


#debug stuff
for n in range(0, len(grid)):
    for x in range(0, len(grid[n])):
        print grid[n][x].get_kind()


display_grid() #doesnt work yet. mostly because how do I python 






