def intersectionArrays(nums1, nums2):
    output = []
    
    for num in nums1:
        if num in nums2:
            output.append(num)
            nums2.remove(num)

    return output

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersectionArrays(nums1, nums2))