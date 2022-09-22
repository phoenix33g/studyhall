class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m = len(nums1)
        n = len(nums2)
        # base-case
        if m == 1 and n == 1: return (nums1[0] + nums2[0]) / 2
        # divide and conquer
        mid = (m + n) // 2
        twoMP = (m + n) / 2 == mid
        if twoMP: mid -= 1
        n1 = 0
        n2 = 0
        while n1 < m and n2 < n:
            if nums1[n1] < nums2[n2]:
                n1 += 1
            else:
                n2 += 1
            if n1 + n2 == mid and n1 < m and n2 < n:
                if nums1[n1] < nums2[n2]:
                    f1 = nums1[n1]
                    n1 += 1
                else:
                    f1 = nums2[n2]
                    n2 += 1
                if not twoMP:
                    return f1
                else:
                    if nums1[n1] < nums2[n2]:
                        f2 = nums1[n1]
                        n1 += 1
                    else:
                        f2 = nums2[n2]
                        n2 += 1
                    return (f1 + f2)/2
        if n1 < m:
            f = mid - n2
            if not twoMP:
                return nums1[f]
            else:
                return (nums1[f] + nums1[f+1]) / 2
        if n2 < m:
            f = mid - n1
            if not twoMP:
                return nums2[f]
            else:
                return (nums2[f] + nums2[f+1]) / 2
                    
                    
s = Solution()
print(s.findMedianSortedArrays([1,2],[3,4]))