import sys

def find_fine(da,ma,ya,de,me,ye):
    if ya<ye:
        return 0
    elif ya==ye:
        if ma<me:
            return 0
        elif ma==me:
            if da<=de:
                return 0
            else:
                return 15 * (da-de)
        else:
            return 500 * (ma-me)
    else:
        return 10000


if __name__ == "__main__":
    da,ma,ya = list(map(int,input().strip().split()))
    de,me,ye = list(map(int,input().strip().split()))
    fine = find_fine(da,ma,ya,de,me,ye)
    print(fine)