import sys
import Queue
import math
import copy

# Node class keeps internal state. Used for "informed" search


class Node:

    def __init__(self):
        self.kind = -1  # Either 0, 1, or 2 meaning empty, wall, or ramen
        self.has_agent = 0  # for knowing the current location
        self.g = 0  # g value for a*  movement cost from start
        self.h = 0  # h value for a* heuristic
        self.f = 0  # f value for a*; g + h
        self.parent = [0, 0]  # for determining path
        self.location = [0, 0]  # to know its location in the grid
        self.state = 0  # 0, 1, 2  (new, frontier, explored)

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
        self.has_agent = x

    def get_occupied(self):
        return self.has_agent

    def set_state(self, state):
        self.state = x

    def get_state(self):
        return self.state

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

grid = []
blankgrid = []
start = [-1, -1]
goal = [0, 0]
flag = 0
steps = []


# takes grid as parameter, and prints to screen what original input file
# looks like but with updated locations for the '@' symbol
def display_grid(gd):
    for n in range(0, len(gd)):
        line_str = ''
        for x in range(0, len(gd[n])):
            if gd[n][x].get_occupied() == 1:
                line_str = line_str + '@'
            elif gd[n][x].get_kind() == 0:
                line_str = line_str + '.'
            elif gd[n][x].get_kind() == 1:
                line_str = line_str + '#'
            elif gd[n][x].get_kind() == 2:
                line_str = line_str + '%'
        print (line_str)


# displays input map with specified location for agent
def display_grid_with_agent(gd, agent):
    for n in range(0, len(gd)):
        line_str = ''
        for x in range(0, len(gd[n])):
            if agent[0] == n and agent[1] == x:
                line_str = line_str + '@'
            elif gd[n][x].get_occupied() == 1:
                line_str = line_str + '@'
            elif gd[n][x].get_kind() == 0:
                line_str = line_str + '.'
            elif gd[n][x].get_kind() == 1:
                line_str = line_str + '#'
            elif gd[n][x].get_kind() == 2:
                line_str = line_str + '%'
        print (line_str)


# heuristic function for estimating cost
def heuristic(location):
    if flag == 0:
        # manhattan
        return abs(location[0] - goal[0]) + abs(location[1] - goal[1])
    elif flag == 1:
        # euclidean
        return math.sqrt(((location[0] - goal[0]) ** 2) +
                         ((location[1] - goal[1]) ** 2))
    else:
        # made_up
        man = abs(location[0] - goal[0]) + abs(location[1] - goal[1])
        euc = math.sqrt(((location[0] - goal[0]) ** 2) +
                        ((location[1] - goal[1]) ** 2))
        return (man + euc) / 2.0


# returns a list of possible nodes to explore,
# not including walls or ones already in fronteir
def get_neighbors(node):
    neighbors = []
    location = node.get_location()

    if not ((location[0] - 1) < 0):
        up_node = grid[location[0] - 1][location[1]]
        if up_node.get_kind() != 1:
            if (up_node.get_state() != 1):
                neighbors.append(up_node)
    if ((location[0] + 1) < len(grid)):
        down_node = grid[location[0] + 1][location[1]]
        if down_node.get_kind() != 1:
            if (down_node.get_state() != 1):
                neighbors.append(down_node)
    if ((location[1] + 1) < len(grid[0])):
        right_node = grid[location[0]][location[1] + 1]
        if right_node.get_kind() != 1:
            if (right_node.get_state() != 1):
                neighbors.append(right_node)
    if not ((location[1] - 1) < 0):
        left_node = grid[location[0]][location[1] - 1]
        if left_node.get_kind() != 1:
            if (left_node.get_state() != 1):
                neighbors.append(left_node)

    return neighbors


# A star algorithm implementation
def a_star():
    explored = set()
    frontier = Queue.PriorityQueue(0)
    start_node_f = heuristic(start)
    grid[start[0]][start[1]].set_f(start_node_f)
    frontier.put((start_node_f, grid[start[0]][start[1]]))
    if start[0] == -1:
        return 0
    while not frontier.empty():
        current_node = frontier.get()[1]
        if current_node.get_kind() == 2:  # goal node
            return 1  # path found
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
                    if (n.get_state() != 1):
                        n.set_state(1)
                        frontier.put((f, n))
    return 0


# traverses nodes from ramen to start ocation building a queue
# uses the queue to display the path agent takes from start to ramen
def print_steps():
    more_steps = True
    path = Queue.LifoQueue(0)
    path.put(goal)
    temp_location = grid[goal[0]][goal[1]].get_parent()
    count = 1
    while more_steps:
        if grid[temp_location[0]][temp_location[1]].get_occupied() == 1:
            more_steps = False
            continue
        path.put(temp_location)
        temp_location = grid[temp_location[0]][temp_location[1]].get_parent()

    while not path.empty():
        print ("step " + str(count) + ":")
        count += 1
        display_grid_with_agent(blankgrid, path.get())


# Start of program execution
# file IO. Taken from lecture slides
if(len(sys.argv)) != 3:
    print ("Wrong number of arguments -- use python_file map_file heuristic")
    raise SystemExit(1)  # throw an error and exit
f = open(sys.argv[1])  # program name is argv[0]

heur = sys.argv[2]
if heur == "manhattan":
    flag = 0
elif heur == "euclidean":
    flag = 1
elif heur == "made_up":
    flag = 2
else:
    print ("Incorrect heuristic -- use manhattan, euclidean, or made_up")
    raise SystemExit(1)  # throw an error and exit

lines = f.readlines()  # reads all lines into list one go
f.close()

# this cleans up the lines and makes each line into a list itself.
# used to cunstruct the list of nodes
for n in range(0, len(lines)):
    lines[n] = list(lines[n].strip())

# builds internal representation of input map, using a 2d list of Nodes
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
            goal = [n, x]
        if lines[n][x] == '@':
            node.set_occupied(1)
            start = [n, x]
        node.set_location([n, x])
        li.append(node)
    grid.append(li)


# a version of grid without agent
blankgrid = copy.deepcopy(grid)
for n in range(0, len(blankgrid)):
        for x in range(0, len(blankgrid[n])):
            if blankgrid[n][x].get_occupied() == 1:
                blankgrid[n][x].set_occupied(0)

# run algorithm, dispaly result
solution = a_star()
if solution == 0:
    print ('There is no path to ramem :(')
else:
    print ('Initial:')
    display_grid(grid)
    print_steps()
    print ('YAY NOM NOM NOM')
