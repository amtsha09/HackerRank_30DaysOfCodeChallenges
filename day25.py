############# Day 25 #################

import math

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    
    T = int(input())
    n = [int(input()) for i in range(T)]

    for number in n:
        a=prime(number)
        if a:
            print("Prime")
        else:
            print("Not prime")