import sys

if __name__ == "__main__":

    n = int(input().strip())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    swap = 0
    for i in range(len(a)):
        s = 0
        for j in range(len(a)-1):
            if a[s]>a[s+1]:
                temp = a[s]
                a[s] = a[s+1]
                a[s+1]=temp
                swap +=1
            s += 1

    print("Array is sorted in",swap,"swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])