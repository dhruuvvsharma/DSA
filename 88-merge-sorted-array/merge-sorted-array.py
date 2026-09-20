class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1 # num1 ke  last se shuru for num1[i]
        j = n - 1 # nume2 ke last se shuru
        k = m + n - 1 #num1 ke last se shuru but for new num1[k]

        while (i>= 0 and j>= 0):

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
        # Copy any remaining elements from nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        