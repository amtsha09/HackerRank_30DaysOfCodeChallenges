# Day 26 #################

import sys
da,ma,ya = list(map(int,input().strip().split()))
de,me,ye = list(map(int,input().strip().split()))

if ya<ye:
    fine = 0
elif ya==ye:
    if ma<me:
        fine = 0
    elif ma==me:
        if da<=de:
            fine = 0
        else:
            fine = 15 * (da-de)
    else:
        fine = 500 * (ma-me)
else:
    fine = 10000

print(fine)

