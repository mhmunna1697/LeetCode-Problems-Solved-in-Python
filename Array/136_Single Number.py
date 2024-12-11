def singleNumber(nums):
    result = 0
    for n in nums:
        result = n ^ result
    return result

nums = [4,1,2,1,2]
print(singleNumber(nums))