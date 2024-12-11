def mejElement(nums):
    result = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == result:
            count+=1
        elif nums[i] != result:
            if count > 0:
                count-=1
            else:
                result = nums[i]
                count+=1

    return result

nums = [2,2,1,1,1,2,2]

print(mejElement(nums))