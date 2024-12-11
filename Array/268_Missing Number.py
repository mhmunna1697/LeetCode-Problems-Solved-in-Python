def missingNum (nums):
    result = len(nums)
    for i in range (len(nums)):
        result+= i-nums[i]

    return result


nums = [9,6,4,2,3,5,7,0,1]
print(missingNum(nums))