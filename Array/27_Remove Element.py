def Remove_element(nums, val):
    k =0
    for i in range(0, len(nums)):
        if nums[i]!=val:
            nums[k]=nums[i]
            k+=1

    del nums[k:]    
    return nums

nums = [0,1,2,2,3,0,4,2]
val = 2
print(Remove_element(nums,val))

