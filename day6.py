############# Day 6 #################

if __name__ == "__main__":
    integer = int(input())
    string=[]
    for i in range(integer):
        string.append(input())
    
    for s in string:
        odd = ""
        even = ""
        for index,letter in enumerate(s):
            if index%2 == 0:
                even += letter
            else:
                odd += letter
        print(even, odd)

