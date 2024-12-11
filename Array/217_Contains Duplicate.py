def containDup(nums):
    mySet = set()
    for n in nums:
        if n in mySet:
            return True
        mySet.add(n)
    return False

nums = [1,2,3,4]
print(containDup(nums))