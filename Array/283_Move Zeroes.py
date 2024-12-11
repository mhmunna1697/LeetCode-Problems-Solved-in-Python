def moveZero(num):
    p = 0

    for i in range(len(num)):
        if num[i] != 0:
            num[p] = num[i]
            p +=1

    for j in range (len(num)-p):
        num[j+p] = 0
    
    return num



nums = [0,1,0,3,12]
print(moveZero(nums))