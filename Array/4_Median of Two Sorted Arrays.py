def median(arr1, arr2):
    mer_arr = []
    for i in range(len(arr1)):
        mer_arr.append(arr1[i])
    for i in range(len(arr2)):
        mer_arr.append(arr2[i])
    
    mer_arr.sort()
    n = len(mer_arr)
    if n % 2 !=0:
        med = mer_arr[n//2]
    else:
        med = (mer_arr[n//2] + mer_arr[(n//2)-1]) /2

    return med


nums1 = [1,2]
nums2 = [3,4]
print(median(nums1,nums2))