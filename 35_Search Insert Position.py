def Search_Insert_Position(nums, target):
    low=0
    high=len(nums)-1

    while low <= high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            low=mid+1
        elif nums[mid]>target:
            high=mid-1

    return low

nums = [1,3,5,6]
target = 7

print(Search_Insert_Position(nums,target))