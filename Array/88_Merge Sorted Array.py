def mergedSortedArray(nums1,nums2,m,n):
    k = m+n-1
    while m>0 and n>0:
        if nums1[m-1]>nums2[n-1]:
            nums1[k]=nums1[m-1]
            m-=1
        else:
            nums1[k]=nums2[n-1]
            n-=1
        k-=1
    
    while n>0:
        nums1[k]=nums2[n-1]
        n-=1
        k-=1
        
    return nums1

nums1 = [1]
nums2 = [0]
m=1
n=0
print (mergedSortedArray(nums1,nums2,m,n))