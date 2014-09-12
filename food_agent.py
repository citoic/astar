import sys

class Node:

    def __init__(self):
        self.kind = 0 #Can either be 0, 1, or 2 meaning empty, wall, or ramen
        self.g = 0 #g value for a*
        self.h = 0 #h value for a*
        self.f = 0 #f value for a*
        self.parent = [0, 0] #for determining path; may not need since every step is required to be drawn

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        self.kind = k

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



#file IO. Taken from lecture slides
if(len(sys.argv)) != 2: 
    #notice sys.argv is a list of command-line args and we found its length
    print "Please supply a filename"
    raise SystemExit(1) # throw an error and exit
f = open(sys.argv[1]) #program name is argv[0]
lines = f.readlines() # reads all lines into list one go
f.close()




for n in range(0, len(lines)):
    lines[n] = list(lines[n].strip()) 




print lines
