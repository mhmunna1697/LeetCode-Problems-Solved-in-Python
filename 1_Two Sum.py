def twoSum(nums, target):
    for i in range(1, len(nums)):
        for j in range(0,i):
            if nums[i]+nums[j]==target:
                return [j,i]
    return []

nums = [2,17,7,15,7]
target = 9

print (twoSum(nums, target))