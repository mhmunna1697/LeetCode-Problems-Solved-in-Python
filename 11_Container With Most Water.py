def mostWater(arr):
    maxWater = 0
    l = 0
    r = len(arr) -1
    while l < r:
            if arr[l] < arr[r]:
                localMax = arr[l] * (r-l)
            else:
                localMax = arr[r] * (r-l)

            if localMax > maxWater:
                maxWater = localMax

            if arr[l] < arr[r]:
                l+=1
            else:
                r-=1


    return maxWater


height = [1,8,6,2,5,4,8,3,7]
print(mostWater(height))