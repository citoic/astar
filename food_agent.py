import sys


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

#fval = 