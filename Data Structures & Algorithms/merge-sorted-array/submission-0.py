class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1             # Last valid element in nums1
        j = n - 1             # Last element in nums2
        write = m + n - 1     # Position to fill in nums1

        # Fill nums1 from right to left, so its values aren't overwritten.
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1

            write -= 1
