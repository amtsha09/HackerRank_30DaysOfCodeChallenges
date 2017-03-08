############# Day 8 #################

from sys import stdin

if __name__ == "__main__":
    lines = stdin.read().splitlines()
    
    n = int( lines[0] )
    phoneBook = dict( i.split() for i in lines[1:n+1] )
    
    print( "\n".join(["{0}={1}".format(i, phoneBook[i]) if i in phoneBook else "Not found" for i in lines[n+1:] ]) )