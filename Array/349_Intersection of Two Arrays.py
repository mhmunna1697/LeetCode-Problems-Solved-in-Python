def intersectionArrays(nums1, nums2):
    # output = []
    # for i in range (len(nums1)):
    #     for j in range (len(nums2)):
    #         if nums1[i] == nums2[j]:
    #             if nums1[i] not in output:
    #                 output.append(nums1[i])

    # return output

    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersectionArrays(nums1, nums2))