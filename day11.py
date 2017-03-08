############# Day 11 #################

import sys


def hour_glass_max(arr):
    sum_array = []
    for i in range(4):
        for j in range(4):
            sum_array.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

    return (max(sum_array))


if __name__ == "__main__":
    
    arr = []
    for arr_i in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)
        
    print(hour_glass_max(arr))



