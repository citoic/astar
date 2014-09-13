import sys, Queue

class Node:

    def __init__(self):
        self.kind = -1 #Can either be 0, 1, or 2 meaning empty, wall, or ramen
        self.has_person = 0 #for knowing the current location
        self.g = 0 #g value for a*  movement cost 
        self.h = 0 #h value for a* heuristic 
        self.f = 0 #f value for a*; g + h
        self.parent = [0, 0] #for determining path; may not need since every step is required to be drawn
        self.location = [0, 0] #to know its location in the grid
        self.state = 0 # 0, 1, 2  (new, frontier, explored)

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

    def set_parent(self, parent):
        self.parent = parent

    def set_occupied(self, x):
        self.has_person = x

    def get_occupied(self):
        return self.has_person

    def set_state(self, state):
        self.state = x

    def get_state(self):
        return self.state

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

grid = []
start = [0,0]
goal = [0,0]
flag = 0

#takes grid as input, and prints to screen what original input file looks like but with updated locations for the '@' symbol
def display_grid():
    for n in range(0, len(grid)):
        line_str = ''
        for x in range(0, len(grid[n])):
            if grid[n][x].get_occupied() == 1:
                line_str += '@'
            elif grid[n][x].get_kind() == 0:
                line_str = line_str + '.'
            elif grid[n][x].get_kind() == 1:
                line_str = line_str + '#'
            elif grid[n][x].get_kind() == 2:
                line_str = line_str + '%'
        print line_str

def heuristic(location):
    if flag == 0:
        return abs(location[0] - goal[0]) + abs(location[1] - goal[1]) #manhattan distance

#probably a better way to do this
def get_neighbors(node):
    neighbors = []
    location = node.get_location()
    
    if not ((location[0] - 1) < 0):
        up_node = grid[location[0] - 1][location[1]]
    if ((location[0] + 1) < len(grid)):  
        down_node = grid[location[0] + 1][location[1]]
    if ((location[1] + 1) < len(grid[0])):    
        right_node = grid[location[0]][location[1] + 1]
    if not ((location[1] - 1) < 0):
        left_node = grid[location[0]][location[1] - 1]

    if not ((location[0] - 1) < 0):
        if up_node.get_kind() != 1:
            if (up_node.get_state() != 1) :
                #up_node.set_state(1)
                neighbors.append(up_node)

    if ((location[0] + 1) < len(grid)):
        if down_node.get_kind() != 1:
            if (down_node.get_state() != 1) :
                #down_node.set_state(1)
                neighbors.append(down_node)

    if not ((location[1] - 1) < 0):
        if left_node.get_kind() != 1:
            if (left_node.get_state() != 1) :
                #left_node.set_state(1)
                neighbors.append(left_node)

    if ((location[1] + 1) < len(grid[0])):
        if right_node.get_kind() != 1:
            if (right_node.get_state() != 1):
                #right_node.set_state(1)
                neighbors.append(right_node)

    return neighbors
          

#may need to add fifo queue to keep track of steps so this will run completely and display grid will be called last. 
def a_star():
    explored = set()
    frontier = Queue.PriorityQueue(0)
    start_node_f = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
    grid[start[0]][start[1]].set_f(start_node_f)
    frontier.put((start_node_f, grid[start[0]][start[1]]))
    while not frontier.empty():
        current_node = frontier.get()[1]
        if current_node.get_kind() == 2: #goal node
            return 1 #path found
        explored.add(current_node)
        current_node.set_state(2)
        neighbors = get_neighbors(current_node)
        for n in neighbors:  
            if not (n in explored):
                g = current_node.get_g() + 1
                if (n.get_state() != 1) or (g < n.get_g()): 
                    n.set_parent(current_node.get_location())
                    n.set_g(g)
                    f = g + heuristic(n.get_location())
                    n.set_f(f)
                    if (n.get_state() != 1) :
                        n.set_state(1)
                        frontier.put((f, n))
    return 0





#TODO: handle heuristic args
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
            goal = [n,x]
        if lines[n][x] == '@':
            node.set_occupied(1)
            start = [n,x]
        node.set_location([n, x])
        li.append(node)
    grid.append(li)




print 'Initial:'
display_grid() # 



solution = a_star()

if solution == 0:
    print 'There is no path to ramem :('
else:
    print 'need to implement this feature '

