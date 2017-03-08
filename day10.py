############# Day 10 ################# IMPLEMENTING BINARY

import sys

def binary(n):
    if n != 1:
        div = n//2
        mod.append(n%2)
        return (binary(div))
    else:
        return (mod.append(1))

def check(arr):
    count = 0
    total = 0
    for a in arr:
        if a == 1:
            count +=1
            if count > total:
                total = count
        else:
            count = 0
    return(total)
    
if __name__ == "__main__":
    mod=[]
    n = int(input().strip())
    binary(n)
    print(mod[::-1])
    print(check(mod[::-1]))
    